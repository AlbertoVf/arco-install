import argparse
from src.format_software import export_to_file
from src.installer import install, clear_cache, update, export_scripts
from src.repository_values import RepositoryValues as rv


def main():
    parser = argparse.ArgumentParser(
        description="Install the required packages", exit_on_error=True
    )
    parser.add_argument("-a", "--all", action="store_true", help="Install all software")
    parser.add_argument(
        "-c",
        "--compilable",
        action="store_true",
        help="Install software from AUR, snap...",
    )
    parser.add_argument(
        "-d",
        "--distro",
        action="store_true",
        help="Install software from distribution and communnity",
    )
    parser.add_argument(
        "-s", "--script", action="store_true", help="Run software by command line"
    )
    parser.add_argument(
        "-e", "--export", action="store_true", help="Build bashscript installation file"
    )
    args = parser.parse_args()

    if all(value == False for value in vars(args).values()):
        parser.print_help()
        return
    # else:
    #     export_to_file()

    if args.export:
        export_scripts(rv.ALL)
    else:
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
