#!/bin/bash

software_root="../software"
csv_file="$software_root/software.csv"
json_file="$software_root/software.json"

function format_software() {

	sed -Ee 's/(\s+;)/;/g' \
		-i $csv_file

	jq --slurp --raw-input --raw-output \
		'split("\n") | .[1:] | map(split(";")) | map({"repositorio": .[0], "tags": .[1], "paquete": .[2]})' \
		$csv_file >$json_file

	jq '.[] | select(.repositorio=="community") | .paquete' $json_file >"$software_root/community.json"
	jq '.[] | select(.repositorio=="aur") | .paquete' $json_file >"$software_root/aur.json"
	jq '.[] | select(.repositorio=="snap") | .paquete' $json_file >"$software_root/snap.json"
	jq '.[] | select(.repositorio=="distro") | .paquete' $json_file >"$software_root/distro.json"
	jq '.[] | select(.repositorio=="extra") | .paquete' $json_file >"$software_root/extra.json"
}

format_software
