import os
import subprocess

def convert_webm_to_mp3(folder_path):

    files = os.listdir(folder_path)
    for f in files:
        if f.lower().endswith(".webm"):
            print("Converting:", f)
            webm_path = os.path.join(folder_path, f)

            mp3_name = os.path.splitext(f)[0] + ".mp3"

            mp3_path = os.path.join(folder_path, mp3_name)

            result = subprocess.run(
                [
                    "ffmpeg",
                    "-i", webm_path,
                    "-q:a", "0",
                    "-map", "a",
                    mp3_path,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            if result.returncode == 0 and os.path.exists(mp3_path):
                os.remove(webm_path)

folder = "/mnt/c/Mohit/Music/Head Bop Central"
convert_webm_to_mp3(folder)