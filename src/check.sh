#!/bin/bash

installation_command='sudo pacman'

function info_instalation() {
	tput setaf 5
	printf "\n[ $(date) ]  $1\n"
	tput sgr0
}

function check_installed() {
	return "$installation_command -Q $1"
}

function is_installed() {
	tput setaf 2
	printf "\n[ $(date) ] The package $1 is already installed\n"
	tput sgr0
}

function is_not_installed() {
	tput setaf 3
	printf "\n[ $(date) ] Installing package $1\n"
	tput sgr0
}

function red() {
	printf "\e[1;31m$1\e[0;37m\n"
}

function green() {
	printf "\e[1;32m$1\e[0;37m\n"
}

function blue() {
	printf "\e[1;34m$1\e[0;37m\n"
}

function yellow() {
	printf "\e[1;33m$1\e[0;37m\n"
}

function purple() {
	printf "\e[1;35m$1\e[0;37m\n"
}
