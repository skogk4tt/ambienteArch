import os
import subprocess
import time
import glob
# Revisar si el usuario que ejecuta el script es root
if os.geteuid() == 0:
    print("Este script NO debe ser ejecutado como usuario ROOT")
    exit(1)

# Imprimir el mensaje de confirmacion
print("Este Script revisa si tienes las dependencias necesarias")

# Pedir confirmacion al usuario
while True:
    yn = input("Deseas continuar? [y/N]")
    if yn.lower() == "y":
        break
    elif yn.lower() == "n":
        exit()
    else:
        print("Error: debes escribir 'y' o 'n'\n")

os.system("clear")

# Depencencias ----------
dependencias = [
                "base-devel", "rustup", "pacman-contrib", "bspwm", "polybar", "sxhkd",
			    "alacritty", "brightnessctl", "dunst", "rofi", "lsd",
			    "jq", "polkit-gnome", "git", "playerctl", "mpd",
			    "ncmpcpp", "geany", "ranger", "mpc", "picom",
			    "feh", "ueberzug", "maim", "pamixer", "libwebp", "xdg-user-dirs",
			    "webp-pixbuf-loader", "xorg-xprop", "xorg-xkill", "physlock", "papirus-icon-theme",
			    "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd", "ttf-terminus-nerd", "ttf-inconsolata", "ttf-joypixels",
			    "zsh", "zsh-autosuggestions", "zsh-history-substring-search", "zsh-syntax-highlighting"
                ]

def esta_instalada(paquete):
    exit_code = os.system(f"pacman -Qi {paquete} &> /dev/null")
    return exit_code == 0

print("Revisando dependencias")
for paquete in dependencias:
    if not esta_instalada(paquete):
        os.system(f"sudo pacman -S {paquete} --noconfirm")
        print("")
    else:
        print(f"{paquete} ya existe en el sistema")
        time.sleep(1)
time.sleep(3)
os.system("clear")

# Preparando carpetas ----------
if not os.path.exists(os.path.expanduser("~/.config/user-dirs.dirs")):
    os.system("xdg-user-dirs-update")
    print("Creando xdg-user-dirs")
else:
    print("user-dirs.dirs ya existe")
time.sleep(2)
os.system("clear")

# Descargando Repositorio ----------
if os.path.isdir(os.path.expanduser("~/dotfiles")):
    os.system("rm -rf ~/dotfiles")
print("Clonando repositorio")
os.chdir(os.path.expanduser("~"))
os.system("git clone --depth=1 https://github.com/gh0stzk/dotfiles.git")
time.sleep(2)
os.system("clear")

# Copiando archivos
print("Copiando archivos a sus respectivos directorios")

if not os.path.exists(os.path.expanduser("~/.config")):
    os.makedirs(os.path.expanduser("~/.config"))
if not os.path.exists(os.path.expanduser("~/.local/bin")):
    os.makedirs(os.path.expanduser("~/.local/bin"))
if not os.path.exists(os.path.expanduser("~/.local/share/applications")):
    os.makedirs(os.path.expanduser("~/.local/share/applications"))
if not os.path.exists(os.path.expanduser("~/.local/share/fonts")):
    os.makedirs(os.path.expanduser("~/.local/share/fonts"))
if not os.path.exists(os.path.expanduser("~/.local/share/asciiart")):
    os.makedirs(os.path.expanduser("~/.local/share/asciiart"))

ruta_archivos = os.path.expanduser('~/dotfiles/config/*')

for archivo in glob.glob(ruta_archivos):
    try:
        shutil.copytree(archivo, os.path.expanduser('~/.config/'))
        print(f"{archivo}")
        time.sleep(1)
    except Exception as e:
        print(f"{archivo} {str(e)}")
        time.sleep(1)

# Instalando paru y eww
if not os.system("command -v paru >/dev/null 2>&1"):
    print("Instalando paru")
    os.system("cd")
    os.system("git clone https://aur.archlinux.org/paru-bin.git")
    os.system("cd paru-bin")
    os.system("makepkg -si --noconfirm")
    os.system("cd")
else:
    print("Paru ya esta instalado")

if not os.system("command -v eww >/dev/null 2>&1"):
    print("Instalando eww")
    os.system("paru -S eww --skipreview --noconfirm")
    os.system("rm -rf {paru-bin,.cargo,.rustup}")
    os.system("rm -rf $HOME/.cache/paru/clone/eww")
else:
    print("eww ya esta instalado")

# Servicio MPD
os.system("systemctl --user enable mpd.service")
os.system("systemctl --user start mpd.service")
print("servicio MPD listo")
time.sleep(2)

#
print ("Comprobando si tu shell es zsh")
if os.environ['SHELL'] != "/usr/bin/zsh":
    print("Cambiando tu shell a zsh, se necesita su pass")
    os.system("sudo chsh -s /usr/bin/zsh")
    os.system("zsh")
else:
    print("Tu shell es zsh, Reinicia el equipo")
