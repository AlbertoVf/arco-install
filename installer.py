import os
import json
import time

from sys import stdout


def red():
    stdout.write("\033[1;31m")


def green():
    stdout.write("\033[0;32m")


def blue():
    stdout.write("\033[1;34m")


def yellow():
    stdout.write("\033[1;33m")


def purple():
    stdout.write("\033[1;35m")


def white():
    stdout.write("\033[1;37m")


def is_installed(package: str):
    return os.system(f'pacman -Q {package}') == 0


def read_software(type: str):
    with open('software.json', 'r') as f:
        data = json.load(f)['software']
        return data[type]


def instalacion_ok():
    blue()
    time.sleep(1)
    print("[+] Instalacion completa\n")


def init_installation(msg: str):
    yellow()
    print(f'{msg}\n')
    white()


def menu():
    yellow()
    print("""
    _                 ___           _        _ _
   / \   _ __ ___ ___|_ _|_ __  ___| |_ __ _| | |
  / _ \ | '__/ __/ _ \| || '_ \/ __| __/ _` | | |
 / ___ \| | | (_| (_) | || | | \__ \ || (_| | | |
/_/   \_\_|  \___\___/___|_| |_|___/\__\__,_|_|_|
""")
    purple()
    print(""" [1] Instalacion completa\n [2] Instalacion de paquetes community\n [3] Instalacion de paquetes aur\n [4] Instalacion de paquetes snap\n [5] Instalacion de paquetes extra\n [6] Salir\n """)
    blue()
    option = input("\n[*] Seleccione una opcion: ")

    if option == "1":
        aur()
        community()
        snap()
        extra()
    if option == "2":
        community()
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

    for i in read_software('aur'):
        if is_installed(i):
            green()
            print(f'[-] {i} ya esta instalado')
        else:
            yellow()
            print(f'[+] Instalando {i}')
            os.system(f'git clone https://aur.archlinux.org/{i}.git')
            os.system(f'cd {i}')
            os.system('makepkg -si --needed --noconfirm')
            os.system(f'cd ..')
    instalacion_ok()


def snap():
    init_installation("Instalando paquetes snap...")

    os.system('systemctl enable --now snapd.socket')
    os.system('ln -s /var/lib/snapd/snap /snap')

    for i in read_software('snap'):
        if os.system(f'snap list | grep {i}') == 0:
            green()
            print(f'[-] {i} ya esta instalado')
        else:
            yellow()
            print(f'[+] Instalando {i}')
            os.system(f'snap install {i}')
    instalacion_ok()


def community():
    init_installation("Instalando paquetes de la comunidad...")
    for i in read_software('community'):
        if is_installed(i):
            green()
            print(f'[-] {i} ya esta instalado')
        else:
            yellow()
            print(f'[+] Instalando {i}')
            os.system(f'pacman -Sy --noconfirm --needed {i}')
    instalacion_ok()


def extra():
    init_installation("Instalando paquetes extra...")
    for i in read_software('extra'):
        os.system(i)
    instalacion_ok()
