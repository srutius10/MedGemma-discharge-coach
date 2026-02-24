SYSTEM_PROMPT = """You are a strict medical transcription assistant.
Generate a SOAP note using ONLY the exact words spoken in the conversation below.
STRICT RULES:
- If it was NOT explicitly said, write: Not documented
- Do NOT infer, assume, or add ANY clinical details
- Do NOT add vitals, lab values, or test results unless spoken aloud
- Do NOT add ICD-10 codes unless the doctor stated a formal diagnosis
- Do NOT add medications unless explicitly mentioned by name
- Do NOT add plan steps unless the doctor explicitly stated them
- Do NOT infer diagnosis from medication prescribed. Only document Assessment if doctor says the diagnosis name out loud.
- If a patient mentions running out of or using a specific medication,
  document it under Medications with a note e.g. (ran out) or (PRN use)

Format:
**Subjective:** (patient's own words only)
**Objective:** (only vitals/findings explicitly stated)
**Assessment:** (only diagnoses explicitly named by doctor)
**Plan:** (only instructions explicitly given by doctor)
**Problem List:** (only conditions explicitly named)
**Medications:** (only drugs explicitly mentioned)
**ICD-10 Codes:** (only if formal diagnosis explicitly stated)
"""

EXAMPLES = {
    "Chest Pain": """Doctor: What brings you in today?
Patient: I've had chest tightness for two days, worse when I walk.
Doctor: Any history of heart problems?
Patient: I have high blood pressure and take amlodipine 5mg daily.
Doctor: Let me check your vital signs. Blood pressure is 145/90, heart rate 88, oxygen saturation 97%.
Doctor: I'm going to order an EKG and troponin levels to rule out cardiac issues.""",

    "Diabetes Follow-up": """Doctor: How have you been managing your diabetes?
Patient: Pretty well. I'm taking metformin 1000mg twice daily.
Doctor: Any issues with blood sugar levels?
Patient: My morning readings are usually around 140.
Doctor: Let's check your A1C today. Also, are you having any numbness in your feet?
Patient: No, my feet feel fine.
Doctor: Good. Keep monitoring your sugars and we'll adjust if needed.""",

    "Respiratory Infection": """Doctor: Tell me about your symptoms.
Patient: I've had a fever and cough for 5 days now.
Doctor: Is the cough productive?
Patient: Yes, yellow-green phlegm. And I'm short of breath when I walk.
Doctor: Any chest pain when you breathe?
Patient: A little bit, yes.
Doctor: Let me examine your lungs. I hear crackles in the right lower lobe. Temperature is 101.5°F.
Doctor: This looks like bacterial pneumonia. I'll prescribe azithromycin 500mg for 5 days.""",

    "Migraine": """Doctor: What seems to be the problem?
Patient: I've had a severe throbbing headache on my left side for 3 days.
Doctor: Any nausea or sensitivity to light?
Patient: Yes, both. I feel better in a dark room.
Doctor: Have you had migraines before?
Patient: Yes, occasionally, but this one is worse than usual.
Doctor: I'll prescribe sumatriptan 100mg for the acute episodes."""
}
