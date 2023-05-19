#!/bin/sh

source src/messages.sh
source src/installer.sh

helper() {
	yellow "\nArcoInstall\n
  -a, --aur       : Install software from (AUR) Arch User Repository
  -c, --community : Install software from community repository
  -d, --distro    : Install software from arco-linux repository
  -e, --extra     : Install extra software
  -f, --fonts     : Install nerd fonts
  -s, --snap      : Install snap packages
  -t, --total     : Install all software
  -h, --help      : Print helper
"
}

cli() {

	if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
		helper
	else
		update_packages
		install_necessary_packages
		case $1 in
		-a | --aur)
			install_aur
			;;
		-e | --extra)
			install_extra
			;;
		-s | --snap)
			install_snap
			;;
		-c | --community)
			install_community
			;;
		-d | --distro)
			install_distro
			;;
		-f | --fonts)
            install_fonts
            ;;
		-t | --all)
			install_all
			;;
		esac
	fi
}

cli $@
