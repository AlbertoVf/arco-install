import os
from installer import name, aur, snap, community, extra, root, update, help
import sys


if __name__ == '__main__':
    id = os.getuid()
    name()
    if id == 0:
        root()
    else:
        if len(sys.argv) == 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
            help()
        else:
            update()
            if sys.argv[1] == '--aur' or sys.argv[1] == '-a':
                aur()
            elif sys.argv[1] == '--snap' or sys.argv[1] == '-s':
                snap()
            elif sys.argv[1] == '--extra' or sys.argv[1] == '-e':
                extra()
            elif sys.argv[1] == '--community' or sys.argv[1] == '-c':
                community("community")
            elif sys.argv[1] == '--distro' or sys.argv[1] == '-d':
                community("distro")
            elif sys.argv[1] == '--total' or sys.argv[1] == '-t':
                aur()
                community("community")
                community("distro")
                snap()
                extra()
            else:
                help()
