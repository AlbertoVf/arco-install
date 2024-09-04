import argparse
from arco_install.format_software import export_to_file
from arco_install.installer import install, clear_cache, update, export_scripts
import arco_install


def main():
    parser = argparse.ArgumentParser( description="Install the required packages", exit_on_error=True )
    parser.add_argument("-a", "--all", action="store_true", help="Install all software")
    parser.add_argument("-c", "--compilable", action="store_true", help="Install software from AUR, snap...", )
    parser.add_argument("-d", "--distro", action="store_true", help="Install software from distribution and communnity", )
    parser.add_argument("-s", "--script", action="store_true", help="Run software by command line" )
    parser.add_argument("-e", "--export", action="store_true", help="Build bashscript installation file" )
    args = parser.parse_args()

    export_to_file()
    if all(value == False for value in vars(args).values()):
        parser.print_help()
        return

    if args.export: export_scripts(arco_install.RepositoryValues.ALL)
    else:
        update()
        if args.all: [install(r) for r in arco_install.RepositoryValues.ALL]
        if args.compilable: [install(r) for r in arco_install.RepositoryValues.COMPILABLE]
        if args.distro: [install(r) for r in arco_install.RepositoryValues.DISTRO]
        if args.script: [install(r) for r in arco_install.RepositoryValues.SCRIPT]
        clear_cache()


main()
