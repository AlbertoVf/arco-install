import os
from installer import menu, update, root

if __name__ == '__main__':
    id = os.getuid()

    if id == 0:
        root()
    else:
        update()
        menu()
