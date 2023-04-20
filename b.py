import os
import shutil
import time
import glob

source_folder = os.path.expanduser('~/dotfiles/config/*')
target_folder = os.path.expanduser('~/.config/')

for file_path in glob.glob(source_folder):
    try:
        shutil.copy2(file_path, target_folder)
    except Exception as e:
        print(f"Error copying file {file_path}: {str(e)}")
    time.sleep(1)