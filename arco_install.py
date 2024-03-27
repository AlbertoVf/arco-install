import argparse
import subprocess
from src.format_software import export_to_file
from src.installer import install, clear_cache, update, export_scripts
from src.repository_values import RepositoryValues as rv


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
        help="Install software from distribution and communnity",
    )
    parser.add_argument(
        "-s", "--script", action="store_true", help="Install extra software"
    )
    parser.add_argument(
        "-e", "--export", action="store_true", help="Build bashscript installation file"
    )
    args = parser.parse_args()

    if args.export:
        export_scripts(rv.ALL)
    elif args.help:
        pass
    else:
        export_to_file()
        update()
        if args.distro:
            [install(r) for r in rv.DISTRO]
        if args.script:
            [install(r) for r in rv.SCRIPT]
        if args.compilable:
            [install(r) for r in rv.COMPILABLE]
        if args.all:
            [install(r) for r in rv.ALL]
        clear_cache()


main()
