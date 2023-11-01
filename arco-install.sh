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
		package::format
		install::necessary
		case $1 in
		-a | --aur)
			install::aur
			;;
		-c | --community)
			install::community
			;;
		-d | --distro)
			install::distro
			;;
		-e | --extra)
			install::extra
			;;
		-f | --fonts)
			install::fonts
			;;
		-s | --snap)
			install::snap
			;;
		-t | --total)
			install::total
			;;
		esac
	fi
}

cli $@
