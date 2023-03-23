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

while getopts "haescdt" opt; do
	case ${opt} in
	a)
		install_aur
		;;
	e)
		install_extra
		;;
	s)
		install_snap
		;;
	c)
		install_community
		;;
	d)
		install_distro
		;;
	t)
		install_all
		;;
	h)
		helper
		;;
	\?)
		echo "Opción inválida: -$OPTARG" 1>&2
		exit 1
		;;
	:)
		echo "La opción -$OPTARG requiere un argumento." 1>&2
		exit 1
		;;
	esac
done
