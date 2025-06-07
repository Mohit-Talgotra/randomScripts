import os
import shutil

def move_audio_and_parent_duplicates(parent_folder):

    audio_folder = os.path.join(parent_folder, "audio_files")

    if not os.path.exists(audio_folder):
        return

    parent_files = os.listdir(parent_folder)
    audio_files = os.listdir(audio_folder)

    parent_names = set()
    audio_names = set()

    for f in parent_files:
        p = os.path.join(parent_folder, f)
        if os.path.isfile(p):
            name, ext = os.path.splitext(f)
            parent_names.add(name)

    for f in audio_files:
        p = os.path.join(audio_folder, f)
        if os.path.isfile(p):
            name, ext = os.path.splitext(f)
            if name.endswith("-audio"):
                name = name[:-6]
            audio_names.add(name)

    duplicates = parent_names.intersection(audio_names)

    new_folder = os.path.join(parent_folder, "repeated_files")

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    # Move duplicates from parent folder
    for f in parent_files:
        p = os.path.join(parent_folder, f)
        if os.path.isfile(p):
            name, ext = os.path.splitext(f)
            if name in duplicates:
                shutil.move(p, os.path.join(new_folder, f))

    # Move duplicates from audio_files folder
    for f in audio_files:
        p = os.path.join(audio_folder, f)
        if os.path.isfile(p):
            name, ext = os.path.splitext(f)
            base_name = name
            if name.endswith("-audio"):
                base_name = name[:-6]
            if base_name in duplicates:
                shutil.move(p, os.path.join(new_folder, f))

folder = "/mnt/c/Mohit/Music/Head Bop Central"
move_audio_and_parent_duplicates(folder)