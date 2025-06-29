# 🤖 AI Meeting Assistant

An end-to-end AI-powered assistant that automatically joins Google Meet meetings, records the session using OBS Studio, transcribes the conversation, summarizes the meeting, extracts actionable tasks, and sends those tasks via email to relevant recipients.

---

## 🚀 Features

- ✅ Auto-joins a Google Meet link using Selenium
- 🎥 Records the session using OBS Studio
- 🎧 Transcribes meeting audio using OpenAI's Whisper
- 📝 Summarizes the transcript with Gemini 1.5 Flash
- 📋 Extracts tasks and responsibilities using Gemini AI
- 📧 Sends task-specific emails to each participant

---

## 📁 Project Structure

AI-meeting-assistant/
├── main.py # Main orchestrator
├── .env # Environment variables (keep this secret)
├── requirements.txt # Python dependencies
├── Agents/
│ ├── summarizer_agent.py # Gemini summarization
│ ├── task_splitter_agent.py # Gemini task extraction
│ └── transcriber_agent.py # Whisper transcription
├── services/
│ ├── email_service.py # Sends email notifications
│ └── meet_joiner.py # Google Meet auto-join logic
├── obs_controller.py # Starts & stops OBS recording
├── README.md # This file



## ⚙️ Requirements

- Python 3.9+
- Google Chrome & ChromeDriver
- OBS Studio with WebSocket plugin
- Whisper
- Gemini API access

---

## 📦 Installation

Set up a virtual environment:
python -m venv .venv
.venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Create a .env file and add
GEMINI_API_KEY=your_gemini_api_key
EMAIL=youremail@gmail.com
PASSWORD=your_app_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
🧪 Running the Assistant

python main.py
It will:

Join the meeting

Record for 60 seconds

Transcribe, summarize, extract tasks

Email tasks automatically
