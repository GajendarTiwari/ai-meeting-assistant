import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_tasks(transcript):
    prompt = f"""
    Extract all actionable tasks from the following meeting transcript. 
    For each task, provide the employee's name and their task. 
    Return the result as a valid JSON object with employee names as keys and tasks as values.
    
    Transcript:
    \"\"\"{transcript}\"\"\"
    """

    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)

        raw_text = response.text.strip()

        # Extract JSON from code block (if Gemini wraps it in triple backticks)
        if raw_text.startswith("```json"):
            raw_text = raw_text.strip("```json").strip("`").strip()
        elif raw_text.startswith("```"):
            raw_text = raw_text.strip("```").strip()

        # Attempt to load as JSON
        tasks = json.loads(raw_text)

        if not isinstance(tasks, dict):
            raise ValueError("Parsed tasks is not a dictionary")

        return tasks

    except Exception as e:
        print(f"❌ Task extraction failed: {e}")
        print(f"⚠️ Gemini response was:\n{response.text}")
        return None
