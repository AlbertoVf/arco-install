import os
from installer import menu, red

if __name__ == '__main__':
    id = os.getuid()

    if id == 0:
        red()
        print("\n[!] Es necesario ser usuario root para ejecutar este script")
    else:
        os.system(
            'sudo reflector - f 30 - l 30 - -number 10 - -verbose - -save / etc/pacman.d/mirrorlist')
        os.system('sudo pacman -Sy')
        menu()
