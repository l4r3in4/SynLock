 

import os

LOCK_EXTENSION = ".locked"
RANSOM_NOTE = "READ_ME.txt"
RANSOM_TEXT = """
Your files have been locked by SynLock!

This is an educational ransomware simulator. No real encryption was performed.
"""

def lock_files(target_folder):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if not file.endswith(LOCK_EXTENSION) and file != RANSOM_NOTE:
                old_path = os.path.join(root, file)
                new_path = old_path + LOCK_EXTENSION
                os.rename(old_path, new_path)
        # drop ransom note in every folder
        note_path = os.path.join(root, RANSOM_NOTE)
        with open(note_path, "w") as f:
            f.write(RANSOM_TEXT)
    print(f"Locked files and dropped ransom notes in {target_folder}")

def unlock_files(target_folder):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file.endswith(LOCK_EXTENSION):
                old_path = os.path.join(root, file)
                new_path = old_path[:-len(LOCK_EXTENSION)]
                os.rename(old_path, new_path)
        # remove ransom note
        note_path = os.path.join(root, RANSOM_NOTE)
        if os.path.exists(note_path):
            os.remove(note_path)
    print(f"Unlocked files and removed ransom notes in {target_folder}")

if __name__ == "__main__":
    folder = input("Enter the full path to the folder to lock/unlock: ").strip()
    action = input("Type 'lock' to simulate encryption or 'unlock' to restore files: ").strip().lower()

    if not os.path.isdir(folder):
        print("Invalid folder path.")
        exit(1)

    if action == "lock":
        lock_files(folder)
    elif action == "unlock":
        unlock_files(folder)
    else:
        print("Invalid action.")
