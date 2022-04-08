import os
from installer import menu

if __name__ == '__main__':
    id = os.getuid()

    if id == 0:
        print("\n\033[1;31m[!] Es necesario ser root para ejecutar el script")
    else:
        os.system(
            'sudo reflector -f 30 -l 30 --number 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Sy')
        menu()
