#!/usr/bin/env sh

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
"
}

cli() {
	if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
		helper
	elif [[ $1 == "-l" ]] || [[ $1 == "--log" ]]; then
		log
	else
		packageFormat
		installNecessary
		case $1 in
		-a | --aur)
			installAur
			;;
		-c | --community)
			installCommunity
			;;
		-d | --distro)
			installDistro
			;;
		-e | --extra)
			installExtra
			;;
		-f | --fonts)
			installFonts
			;;
		-s | --snap)
			installSnap
			;;
		-t | --total)
			installTotal
			;;
		esac
	fi
}

cli $@
