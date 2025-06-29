import os
import time
from dotenv import load_dotenv

from Agents.summarizer_agent import summarize_transcript
from Agents.task_splitter_agent import extract_tasks
from Agents.transcriber_agent import transcribe_meeting
from services.email_service import send_task_emails
from obs_controller import start_obs_recording, stop_obs_recording_and_organize
from services.meet_joiner import join_meet

# Load environment variables
load_dotenv()

# Constants
RECORDING_DURATION = 60  # seconds
MEETING_URL = "https://meet.google.com/shj-ugah-niz"

def main():
    print("🚀 Launching Google Meet...")
    try:
        join_meet(MEETING_URL)
    except Exception as e:
        print(f"⚠️ Error joining Meet: {e}")
        return

    print("🎬 Starting OBS recording...")
    try:
        start_obs_recording()
    except Exception as e:
        print(f"❌ Failed to start OBS recording: {e}")
        return

    print(f"⏳ Recording for {RECORDING_DURATION} seconds...")
    time.sleep(RECORDING_DURATION)

    print("🛑 Stopping OBS recording...")
    try:
        recorded_file = stop_obs_recording_and_organize()
        if not recorded_file:
            print("❌ No recorded file found.")
            return
    except Exception as e:
        print(f"❌ Failed to stop and organize OBS recording: {e}")
        return

    print(f"🎧 Transcribing audio from: {recorded_file}")
    try:
        transcript = transcribe_meeting(recorded_file)
    except Exception as e:
        print(f"❌ Transcription failed: {e}")
        return

    print("📝 Summarizing transcript...")
    try:
        summary = summarize_transcript(transcript)
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
        return

    print("✅ Summary:")
    print(summary)

    print("📋 Extracting tasks...")
    try:
        tasks = extract_tasks(summary)
        if not tasks or not isinstance(tasks, dict):
            print("❌ Invalid task format. Expected a dictionary.")
            return
        print("📌 Extracted Tasks:")
        for name, task in tasks.items():
            print(f"  - {name}: {task}")
    except Exception as e:
        print(f"❌ Task extraction failed: {e}")
        return

    print("📬 Sending task emails...")
    try:
        send_task_emails(tasks)
    except Exception as e:
        print(f"❌ Failed to send emails: {e}")
        return

    print("✅ All tasks completed successfully.")

if __name__ == "__main__":
    main()
