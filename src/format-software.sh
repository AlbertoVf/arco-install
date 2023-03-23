#!/bin/bash
source src/check.sh

software_root="software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"

installation_command='sudo pacman'

function info_instalation() {
	blue "[ $(date) ]  $1"
}

function check_installed() {
	return "$installation_command -Q $1"
}

function is_installed() {
	green "[ $(date) ] The package $1 is already installed"
}

function is_not_installed() {
	yellow "[ $(date) ] Installing package $1"
}

function format_software() {
	jq -sRrc 'split("\n") | .[1:] | map(split(";")) | map({"repositorio": .[0], "tags": .[1], "paquete": .[2]})' \
		$csv_file >$json_file

	sed -Ee 's/(\s+\")/\"/g' -i $json_file
	green "Software files updated"
}

function update_packages() {
	format_software
	blue "Updating packages"
	sudo reflector --verbose -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist
	$installation_command -Syyu
}
