#!/bin/bash
source src/check.sh

software_root="software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"


function info_instalation() {
	blue "[ $(date) ] $1"
}

function is_installed() {
	green "[ $(date) ] The package $1 is already installed"
}

function is_not_installed() {
	red "[ $(date) ] Installing package $1"
}

function format_software() {
	jq -sRrc 'split("\n") | .[1:] | map(split(";")) | map({"paquete": .[2], "repositorio": .[0], "tags": .[1]})' \
		$csv_file >$json_file

	sed -Ee 's/(\s+\")/\"/g' -i $json_file
	green "Software files updated"
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
	format_software
fi
