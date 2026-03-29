# 🎙️ VERNAI – VoiceHealth AI

**Voice-First Healthcare Guidance for India’s Underserved**

---

## 🚨 Problem

A large portion of India’s population relies on **regional languages and voice interaction**, yet most digital healthcare tools are:

* Text-heavy
* English-first
* Difficult for low-literacy users

This leads to:

* Misunderstanding of basic symptoms
* Delayed preventive action
* Unnecessary clinic visits
* Lack of awareness about financial preparedness

---

## 💡 Solution

**VoiceHealth AI** is a **voice-first healthcare assistant** that provides:

* 🗣️ Regional language interaction (Hindi, Tamil → scalable)
* 🛡️ Safe, non-diagnostic health guidance
* 📍 Region-aware advisories (seasonal + local data)
* 💬 WhatsApp-style accessibility (low adoption friction)

👉 Designed for **people who cannot or prefer not to type/read**

---

## ⚙️ How It Works

1. **User speaks** in regional language
2. **ASR (Speech-to-Text)** converts voice → text
3. **Intent Detection (NLP)** identifies health concern
4. **Guardrail Engine**:

   * Blocks diagnosis
   * Detects emergency cases
5. **Intent → Advisory Mapping**:

   * Maps input to verified public health guidance
6. **Response Generation**:

   * Template-based, rule-constrained
   * No open-ended AI output
7. **Text-to-Speech (TTS)** returns response in user’s language

---

## 🧠 System Design Principles

* **Voice-first, not voice-enabled**
* **Safety over completeness**
* **Verified knowledge only (no hallucination)**
* **Low cognitive load for users**

---

## 🛡️ Safety & Guardrails

* ❌ No medical diagnosis
* ❌ No treatment prescriptions
* ✅ Only preventive & awareness guidance
* ✅ Emergency escalation detection
* ✅ Controlled responses from verified sources

> All responses are template-based and constrained to trusted public health advisories.

---

## 📊 Data Sources

* Ministry of Health and Family Welfare (MoHFW)
* Indian Council of Medical Research (ICMR)
* State health bulletins
* WHO public health recommendations

👉 No personal health data is used.

---

## 🧪 Validation Approach

* **ASR Testing** → accuracy of regional speech transcription
* **Intent Mapping** → correct advisory selection
* **Latency Check** → <5–10 seconds response time

---

## 👤 Example Use Case

**Priya (58, rural Maharashtra)**

* Speaks in Hindi: *“Mere pote ko bukhar hai, kya karu?”*
* System:

  * Detects fever-related concern
  * Checks seasonal advisory (e.g., dengue/viral)
  * Responds with:

    * Basic care steps
    * Warning signs
    * When to visit a doctor

👉 No diagnosis. No jargon. Clear voice guidance.

---

## 🚀 What Makes It Different

| Feature      | VoiceHealth AI  | General Chatbots | Health Apps      |
| ------------ | --------------- | ---------------- | ---------------- |
| Interface    | Voice-first     | Text-first       | Text-heavy       |
| Language     | Regional        | Mostly English   | Mostly English   |
| Safety       | Guardrail-based | Open-ended       | Limited          |
| Context      | Region-aware    | Generic          | Generic          |
| Target Users | Low-literacy    | Tech-savvy       | Smartphone users |

---

## ⚙️ Tech Stack (Conceptual)

* **ASR**: Whisper / Multilingual Speech Models
* **NLP**: LLM + Rule-based Intent Classification
* **Backend**: Python / Node.js
* **Deployment**: WhatsApp API (Twilio)
* **TTS**: Regional language speech synthesis

---

## ⚠️ Challenges

* ASR accuracy across accents
* Limited regional health datasets
* Balancing safety vs helpfulness
* Building trust among rural users

---

## 🔮 Future Scope

* Add more Indian languages (Marathi, Bengali, etc.)
* Offline / low-connectivity support
* Integration with government health services
* Voice biomarker-based early risk detection (advanced)

---

## ⚠️ Disclaimer

VoiceHealth AI provides **informational guidance only**.
It does **not** offer:

* Medical diagnosis
* Treatment advice
* Financial recommendations

It is designed to **support awareness**, not replace healthcare professionals.

---

## 🏁 Summary

VoiceHealth AI is not just an AI tool —
it’s a **bridge between healthcare knowledge and people who are currently excluded from it**.

---
