import argparse
import subprocess
from src.installer import *

def main():
    parser = argparse.ArgumentParser(description="Install the required packages")
    parser.add_argument("-a", "--all", action="store_true", help="Install all software")
    parser.add_argument(
        "-c",
        "--compilable",
        action="store_true",
        help="Install software from AUR, snap",
    )
    parser.add_argument(
        "-d",
        "--distro",
        action="store_true",
        help="Install software from distribuiton and communnity",
    )
    parser.add_argument(
        "-e", "--extra", action="store_true", help="Install extra software"
    )
    args = parser.parse_args()

    if args.distro:
        install("distro")
        install("community")
        install("extra")
    if args.extra:
        install("command")
    if args.compilable:
        install("aur")
        install("snap")
    if args.all:
        install("distro")
        install("community")
        install("extra")
        install("aur")
        install("snap")
        install("command")

# update()
main()