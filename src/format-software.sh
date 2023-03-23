#!/bin/bash
source src/check.sh
software_root="software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"

function format_software() {
	jq -sRrc 'split("\n") | .[1:] | map(split(";")) | map({"repositorio": .[0], "tags": .[1], "paquete": .[2]})' \
		$csv_file >$json_file

	sed -Ee 's/(\s+\")/\"/g' -i $json_file
	purple "Software files updated"
}
