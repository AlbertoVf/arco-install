#!/bin/sh

software_root="software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"
log='arco-install.log'

log::date() {
	printf "\e[1;34m[ $(date) ] $1.\e[0;37m\n"
}

log::isInstalled() {
	printf "\e[1;32m[ $(date) ] The package $1 is already installed.\e[0;37m\n"
}

log::isNotInstalled() {
	printf "\e[1;33m[ $(date) ] Installing package $1.\e[0;37m\n"
}

package::format() {
	jq -sRrc 'split("\n") | .[2:] | map(split(";")) | map({"name": .[0], "repository": .[2], "tags": .[1]})' \
		$csv_file >$json_file

	sed -Ee 's/(\s+\")/\"/g' -i $json_file
	log::date "Software file updated"
}

log(){
	contenido=$(cat $log)
	echo -e "$contenido"
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
	package::format
fi