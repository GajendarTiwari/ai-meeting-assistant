# 🤖 AI Meeting Assistant

An end-to-end AI-powered assistant that **automatically joins Google Meet meetings**, records the session using OBS Studio, **transcribes** the conversation, **summarizes** the meeting, **extracts actionable tasks**, and **sends those tasks via email** to the appropriate recipients.

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

<pre>
AI-meeting-assistant/
├── main.py                  # Main orchestrator
├── .env                     # Environment variables (keep this secret)
├── requirements.txt         # Python dependencies
├── Agents/
│   ├── summarizer_agent.py    # Gemini summarization
│   ├── task_splitter_agent.py # Gemini task extraction
│   └── transcriber_agent.py   # Whisper transcription
├── services/
│   ├── email_service.py       # Sends email notifications
│   └── meet_joiner.py         # Google Meet auto-join logic
├── obs_controller.py        # Starts & stops OBS recording
├── README.md                # This file
</pre>

---

## ⚙️ Requirements

- Python 3.9+
- Google Chrome + ChromeDriver
- OBS Studio (with WebSocket plugin)
- Whisper (via OpenAI or Whisper.cpp)
- Gemini 1.5 API key (Google AI Studio)
- Gmail with App Password (for SMTP sending)

---

## 📦 Installation

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

Create a .env file in the project root with the following content:

env
GEMINI_API_KEY=your_gemini_api_key

# Gmail credentials
EMAIL=youremail@gmail.com
PASSWORD=your_app_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=your port number

Running the Assistant
python main.py

The assistant will:

✅ Auto-join the Google Meet

🎥 Record the session for 60 seconds

🎧 Transcribe the meeting audio

📝 Summarize the discussion

📋 Extract tasks from the summary

📧 Send emails with assigned tasks

🛡️ Disclaimer
This is for educational and automation demonstration purposes only.

Use it responsibly, respecting privacy, terms of service, and legal obligations.

📫 Contact
If you'd like to contribute or report bugs, feel free to create an issue or pull request.
