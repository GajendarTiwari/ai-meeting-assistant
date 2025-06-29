# obs_controller.py

import time
import os
import glob
import shutil
from datetime import datetime
from obswebsocket import obsws, requests

# Start OBS recording
def start_obs_recording():
    try:
        ws = obsws("localhost", 4455, "")
        ws.connect()
        ws.call(requests.StartRecord())
        ws.disconnect()
        print("🎬 OBS recording started.")
    except Exception as e:
        print(f"❌ Failed to start OBS recording: {e}")

# Stop OBS recording and organize file
def stop_obs_recording_and_organize():
    try:
        ws = obsws("localhost", 4455, "")
        ws.connect()
        ws.call(requests.StopRecord())
        ws.disconnect()
        print("🛑 OBS recording stopped.")
    except Exception as e:
        print(f"❌ Failed to stop OBS recording: {e}")
        return None

    time.sleep(5)  # allow time for file to save

    # OBS default recording directory
    default_path = os.path.expanduser("C:/Users/Admin/Videos")

    # Get the latest .mp4 file
    mp4_files = glob.glob(os.path.join(default_path, "*.mp4"))
    if not mp4_files:
        print("❌ No .mp4 file found in default OBS folder.")
        return None

    latest_file = max(mp4_files, key=os.path.getctime)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"meeting_recording_{timestamp}.mp4"
    new_path = os.path.join(default_path, new_filename)

    try:
        shutil.move(latest_file, new_path)
        print(f"✅ Recording saved as: {new_path}")
        return new_path
    except Exception as e:
        print(f"❌ Failed to rename/move recording: {e}")
        return None
