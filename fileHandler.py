import os
import shutil

def move_non_audio_files(folder_path):
    unknown_folder = os.path.join(folder_path, 'unknown_files')

    if not os.path.exists(unknown_folder):
        os.makedirs(unknown_folder)

    allowed_extensions = ['.mp3', '.webm']

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext not in allowed_extensions:
                destination = os.path.join(unknown_folder, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename}")

# Replace with your folder path (use WSL style if running inside WSL)
folder = "/mnt/c/Mohit/Music"
move_non_audio_files(folder)