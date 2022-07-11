import os
import json
import time


red = "\033[1;31m"
green = "\033[0;32m"
blue = "\033[1;34m"
yellow = "\033[1;33m"
purple = "\033[1;35m"
white = "\033[1;37m"


installation_command = "sudo pacman"
def root(): print("\033[1;31m[!] Es necesario ser root")


def help():
    print("""
    -h, --help : Muestra esta ayuda
    -a, --aur: Instala el software desde Arch User Repository
    -e, --extra: Instala software extra
    -s, --snap: Instala paquetes snap
    -c, --comunnity: Instala el software desde repositorios oficiales
    -d, --distro: Instala software propio de la distribucion
    -t, --total: Instala todo es software
    """)


def update():
    print("Actualizando repositorios")
    os.system(
        'sudo reflector -f 30 -l 30 --number 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Sy')


def is_installed(package: str):
    return os.system(f'{installation_command} -Q {package}') == 0


def read_software(type: str):
    with open('software.json', 'r') as f:
        data = json.load(f)['software']
        return data[type]


def instalacion_ok():
    time.sleep(1)
    print(f"{blue}[+] Instalacion completa\n")


def init_installation(msg: str):
    print(f'{yellow}{msg}\n{white}')


def name():
    print(f"""{yellow}
    _                 ___           _        _ _
   / \   _ __ ___ ___|_ _|_ __  ___| |_ __ _| | |
  / _ \ | '__/ __/ _ \| || '_ \/ __| __/ _` | | |
 / ___ \| | | (_| (_) | || | | \__ \ || (_| | | |
/_/   \_\_|  \___\___/___|_| |_|___/\__\__,_|_|_|
""")


def menu():
    name()
    print(f"""{purple} [1] Instalacion completa\n [2] Instalacion de paquetes community\n [3] Instalacion de paquetes aur\n [4] Instalacion de paquetes snap\n [5] Instalacion de paquetes extra\n [6] Salir\n """)

    option = input(f"\n{blue}[*] Seleccione una opcion: ")

    if option == "1":
        aur()
        community("community")
        community("distro")
        snap()
        extra()
    if option == "2":
        community("community")
        community("distro")
    if option == "3":
        aur()
    if option == "4":
        snap()
    if option == "5":
        extra()
    if option == "6":
        exit()


def aur():
    init_installation("Instalando paquetes de AUR...")
    os.system("mkdir -p repos; cd repos")
    for i in read_software('aur'):
        if is_installed(i):
            print(f'{green}[-] {i} ya esta instalado')
        else:
            print(f'{yellow}[+] Instalando {i}')
            os.system(
                f'git clone https://aur.archlinux.org/{i}.git && cd {i} && makepkg -si --noconfirm && cd ..')
    instalacion_ok()


def snap():
    init_installation("Instalando paquetes snap...")
    os.system(
        'systemctl enable --now snapd.socket && ln -s /var/lib/snapd/snap /snap')

    for i in read_software('snap'):
        if os.system(f'snap list | grep {i}') == 0:
            print(f'{green}[-] {i} ya esta instalado')
        else:
            print(f'{yellow}[+] Instalando {i}')
            os.system(f'snap install {i}')
    instalacion_ok()


def community(software="community"):
    init_installation("Instalando paquetes de la comunidad...")
    for i in read_software(software):
        if is_installed(i):
            print(f'{green}[-] {i} ya esta instalado')
        else:
            print(f'{yellow}[+] Instalando {i}')
            os.system(f'{installation_command} -Sy --noconfirm --needed {i}')
    instalacion_ok()


def extra():
    init_installation("Instalando paquetes extra...")
    for i in read_software('extra'):
        os.system(i)
    instalacion_ok()
