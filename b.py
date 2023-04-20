import os
import shutil
import time

source_folder = os.path.expanduser('~/dotfiles/config/')
target_folder = os.path.expanduser('~/.config/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    exit(1)

print("Files copied successfully!")
time.sleep(3)