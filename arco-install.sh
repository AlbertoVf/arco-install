#!/bin/bash

source src/check.sh
source src/installer.sh

function helper() {
	yellow "\nArcoInstall"
	purple "
	-h: Muestra esta ayuda
	-a: Instala el software desde Arch User Repository
	-e: Instala software extra
	-s: Instala paquetes snap
	-c: Instala el software desde repositorios oficiales
	-d: Instala software propio de la distribucion
	-t: Instala todo el software
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
