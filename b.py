import os
import shutil
import time

# Copiando archivos
print("Copiando archivos a sus respectivos directorios")

source_folder = os.path.expanduser('~/dotfiles/config/')
target_folder = os.path.expanduser('~/.config/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

source_folder = os.path.expanduser('~/dotfiles/misc/bin/')
target_folder = os.path.expanduser('~/.local/bin/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

source_folder = os.path.expanduser('~/dotfiles/misc/applications/')
target_folder = os.path.expanduser('~/.local/share/applications/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

source_folder = os.path.expanduser('~/dotfiles/misc/fonts/')
target_folder = os.path.expanduser('~/.local/share/fonts/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

source_folder = os.path.expanduser('~/dotfiles/misc/asciiart/')
target_folder = os.path.expanduser('~/.local/share/asciiart/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

source_folder = os.path.expanduser('~/dotfiles/misc/firefox/')
target_folder = os.path.expanduser('~/.mozilla/firefox/*.default-release/')

try:
    shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
    time.sleep(1)
except Exception as e:
    print(f"Error copying files: {str(e)}")
    time.sleep(1)

os.system("cp -f $HOME/dotfiles/home/.zshrc $HOME")
os.system("fc-cache -rv >/dev/null 2>&1")
print("Files copied successfully!!")
time.sleep(3)
