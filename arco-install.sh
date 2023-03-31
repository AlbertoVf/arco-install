#!/bin/bash

source src/messages.sh
source src/installer.sh

function helper() {
	yellow "\nArcoInstall\n
  -h, --help      : Muestra esta ayuda
  -a, --aur       : Instala el software desde Arch User Repository
  -e, --extra     : Instala software extra
  -s, --snap      : Instala paquetes snap
  -c, --community : Instala el software desde repositorios oficiales
  -d, --distro    : Instala software propio de la distribucion
  -t, --total     : Instala todo el software
"
}

function cli() {

	if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
		helper
	else
		update_packages
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
		-t | --all)
			install_all
			;;
		esac
	fi
}

cli $@
