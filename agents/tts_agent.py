"""
agents/tts_agent.py
TTS Agent — Sarvam AI (Bulbul V3)
Fully compatible with current Sarvam API (March 2026)
"""

import httpx
from core.config import settings

SARVAM_TTS_URL = "https://api.sarvam.ai/text-to-speech"

# Valid voices for Bulbul V3
VOICE_MAP = {
    "hi": "priya",      # Natural female Hindi
    "ta": "rahul",      # Male Tamil
    "en": "priya",
    "mr": "priya",
    "bn": "priya",
    "te": "priya",
    "gu": "priya",
    "default": "meera"
}

async def tts_agent(text: str, language: str = "hi") -> str:
    """
    Converts text to speech using Sarvam Bulbul V3.
    Returns base64 audio string.
    """
    # Sarvam hard limit = 500 characters
    if len(text) > 500:
        print(f"[TTS] ⚠️ Text too long ({len(text)} chars) → truncating")
        text = text[:480] + "..."

    headers = {
        "api-subscription-key": settings.SARVAM_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": [text],
        "target_language_code": f"{language}-IN",
        "speaker": VOICE_MAP.get(language, VOICE_MAP["default"]),
        "pace": 1.0,                    # Supported
        "speech_sample_rate": 16000,    # Good quality
        "enable_preprocessing": True,
        "model": "bulbul:v3"            # Correct latest model
        # pitch and loudness are REMOVED — they are NOT supported on v3
    }

    print(f"[TTS] Requesting {language}-IN audio from Sarvam (Bulbul V3)...")

    async with httpx.AsyncClient(timeout=25) as client:
        resp = await client.post(SARVAM_TTS_URL, headers=headers, json=payload)

        if resp.status_code != 200:
            print(f"❌ [TTS] Sarvam Error {resp.status_code}: {resp.text}")
            resp.raise_for_status()

        audio_b64 = resp.json()["audios"][0]
        print("[TTS] ✅ Audio generated successfully!")

    return audio_b64