#!/bin/sh

source src/installer.sh

helper() {
	printf "\nArcoInstall\n
  -a, --aur       : Install software from (AUR) Arch User Repository
  -c, --community : Install software from community repository
  -d, --distro    : Install software from arco-linux repository
  -e, --extra     : Install extra software
  -f, --fonts     : Install nerd fonts
  -s, --snap      : Install snap packages
  -t, --total     : Install all software
  -h, --help      : Print helper
  -l, --log       : View low file
"
}

cli() {
	if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
		helper
	elif [[ $1 == "-l" ]] || [[ $1 == "--log" ]]; then
		log
	else
		update_packages
		install_necessary_packages
		case $1 in
		-a | --aur)
			install_aur
			;;
		-c | --community)
			install_community
			;;
		-d | --distro)
			install_distro
			;;
		-e | --extra)
			install_extra
			;;
		-f | --fonts)
			install_fonts
			;;
		-s | --snap)
			install_snap
			;;
		-t | --total)
			install_total
			;;
		esac
	fi
}

cli $@
