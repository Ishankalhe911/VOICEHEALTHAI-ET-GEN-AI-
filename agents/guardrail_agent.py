"""
agents/guardrail_agent.py
Agent 2: Guardrail — Classifies emergencies, safe queries, AND off-topic inputs.
Powered by Groq (llama-3.3-70b-versatile).
"""

import json
import httpx
import asyncio
from pathlib import Path
from core.config import settings

PROMPT_PATH = Path("prompts/guardrail_prompt.txt")
GROQ_URL    = "https://api.groq.com/openai/v1/chat/completions"

GROQ_HEADERS = {
    "Authorization": f"Bearer {settings.GROQ_API_KEY}",
    "Content-Type":  "application/json",
}

# Hardcoded responses
EMERGENCY_RESPONSE = (
    "मैं आपकी स्थिति समझता हूँ। यह एक आपातकालीन स्थिति लगती है। "
    "कृपया तुरंत नजदीकी अस्पताल जाएं या 112 पर कॉल करें। "
    "I cannot provide a diagnosis. Please see a doctor immediately."
)

OFF_TOPIC_RESPONSE = (
    "कृपया अपना इनपुट चेक करें। "
    "हम केवल genuine health-related मदद के लिए हैं। "
    "Please check your input. We are only for genuine health-related queries."
)

async def guardrail_agent(english_text: str, max_retries: int = 3) -> dict:
    """
    Returns:
        {
            "is_safe":             bool,
            "category":            "A" or "B" or "C",
            "extracted_symptoms":  str,
            "response":            str or None   # emergency or off-topic message
        }
    """
    print("[GUARDRAIL] Analysing safety via Groq (llama-3.3-70b)...")

    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": f"User message: {english_text}"}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.1,
        "max_tokens":  150,
    }

    # Safe default
    result = {"category": "B", "extracted_symptoms": english_text}

    async with httpx.AsyncClient(timeout=10) as client:
        for attempt in range(max_retries):
            try:
                resp = await client.post(GROQ_URL, headers=GROQ_HEADERS, json=payload)
                resp.raise_for_status()

                raw_json = resp.json()["choices"][0]["message"]["content"]
                result   = json.loads(raw_json)
                print(f"[GUARDRAIL] ✅ Category {result.get('category')} | Symptoms: {result.get('extracted_symptoms', '')[:50]}")
                break

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429 and attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"⚠️ [GUARDRAIL] Groq 429. Retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
                    continue
                print(f"❌ [GUARDRAIL] HTTP error: {e.response.text}")
                break

            except (json.JSONDecodeError, KeyError) as e:
                print(f"⚠️ [GUARDRAIL] JSON parse error: {e}. Defaulting to safe.")
                break

    category = result.get("category", "B")
    extracted = result.get("extracted_symptoms", english_text)

    if category == "A":
        return {
            "is_safe": False,
            "category": "A",
            "extracted_symptoms": extracted,
            "response": EMERGENCY_RESPONSE
        }
    elif category == "C":
        return {
            "is_safe": False,
            "category": "C",
            "extracted_symptoms": "",
            "response": OFF_TOPIC_RESPONSE
        }
    else:  # B - safe health query
        return {
            "is_safe": True,
            "category": "B",
            "extracted_symptoms": extracted,
            "response": None
        }