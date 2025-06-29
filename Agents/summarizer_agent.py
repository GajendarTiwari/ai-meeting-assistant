# Agents/summarizer_agent.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_transcript(transcript: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        contents=[{"role": "user", "parts": [f"Summarize this transcript:\n\n{transcript}"]}]
    )

    return response.text
