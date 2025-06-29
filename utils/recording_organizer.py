import os
import shutil
from datetime import datetime

def organize_recording(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file in os.listdir(src_dir):
        if file.endswith(".mp4"):  # or .mp4 if that's your format
            src_path = os.path.join(src_dir, file)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            dest_file = f"Meeting_{timestamp}.mkv"
            dest_path = os.path.join(dest_dir, dest_file)
            shutil.move(src_path, dest_path)
            print(f"[🎞️] Moved and renamed recording to: {dest_path}")
            return dest_path
