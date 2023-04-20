import os
import shutil
import time

source_folder = os.path.expanduser('~/dotfiles/config/')
target_folder = os.path.expanduser('~/.config/')

for dirpath, dirnames, filenames in os.walk(source_folder):
    # Creamos la carpeta de destino si no existe
    target_dir = os.path.join(target_folder, os.path.relpath(dirpath, source_folder))
    os.makedirs(target_dir, exist_ok=True)

    for file_name in filenames:
        source_file_path = os.path.join(dirpath, file_name)
        target_file_path = os.path.join(target_dir, file_name)

        try:
            shutil.copy2(source_file_path, target_file_path)
        except Exception as e:
            print(f"Error copying file {source_file_path}: {str(e)}")
        
        time.sleep(1)
