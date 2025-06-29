import whisper
import os
import datetime

def transcribe_meeting(audio_file_path: str) -> str:
    model = whisper.load_model("base")  # You can also try "small", "medium" for more accuracy
    result = model.transcribe(audio_file_path)

    # Save transcript
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_path = f"data/transcripts/transcript_{timestamp}.txt"
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result['text'])

    return result['text']
