import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}

def ask_healthbot(user_input):
    # Basic Safety Filter
    banned_words = ["prescribe", "diagnose", "treatment plan", "dosage"]
    if any(word in user_input.lower() for word in banned_words):
        return "⚠️ I'm a general health assistant and cannot provide medical treatments or diagnoses. Please consult a certified healthcare professional."

    prompt = f"""
<|system|>
You are a polite, professional, and helpful medical assistant. Always provide safe, general health advice, and encourage users to consult a real doctor for medical issues.
</s>
<|user|>
{user_input}
</s>
<|assistant|>
"""

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if response.status_code != 200:
            return f"⚠️ Error {response.status_code}: {response.text}"

        generated = response.json()

        # Check structure
        if isinstance(generated, list):
            return generated[0]["generated_text"].split("<|assistant|>")[-1].strip()
        elif isinstance(generated, dict) and "generated_text" in generated:
            return generated["generated_text"].strip()
        else:
            return "⚠️ Unexpected response format from the model."

    except Exception as e:
        return f"❌ Exception: {str(e)}"
