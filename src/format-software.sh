#!/bin/sh
source src/messages.sh

software_root="software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"

info_instalation() {
	blue "[ $(date) ] $1"
}

is_installed() {
	green "[ $(date) ] The package $1 is already installed"
}

is_not_installed() {
	yellow "[ $(date) ] Installing package $1"
}

format_software() {
	jq -sRrc 'split("\n") | .[1:] | map(split(";")) | map({"paquete": .[2], "repositorio": .[0], "tags": .[1]})' \
		$csv_file >$json_file

	sed -Ee 's/(\s+\")/\"/g' -i $json_file
	green "Software files updated"
}
