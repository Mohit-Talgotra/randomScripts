import os
import shutil

def move_audio_files(folder_path):

    files = os.listdir(folder_path)

    new_folder = os.path.join(folder_path, "audio_files")

    if not os.path.exists(new_folder):

        os.mkdir(new_folder)

    for f in files:

        if os.path.isfile(os.path.join(folder_path, f)):

            name, ext = os.path.splitext(f)

            if name.endswith("-audio"):

                src = os.path.join(folder_path, f)

                dst = os.path.join(new_folder, f)

                shutil.move(src, dst)

folder = "/mnt/c/Mohit/Music/Head Bop Central"
move_audio_files(folder)