#!/bin/sh
source src/format-software.sh

install_package() {
	name=$1
	if [ -z "$2" ]; then
		command="sudo pacman -Sy --noconfirm --needed"
	else
		command=$2
	fi

	if pacman -Qi $name &>/dev/null; then
		is_installed $name | tee -a $log
	else
		is_not_installed $name | tee -a $log
		$command $name 2>> $log
	fi
}

install_necessary_packages() {
	install_package 'jq' # use to create json file
	install_package 'git' # use to download aur packages
	install_package 'paru' # use to download aur packages
	install_package 'unzip' # use to decompress zip files
	install_package 'snapd' # use to install snap packages
	install_package 'curl' # use to download from url
	format_software
}

update_packages() {
	info_instalation "Updating packages"
	sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Syyu
}

install_aur() {
	info_instalation "Installing aur packages"

	software=($(jq -r '.[] | select(.repository=="aur") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name 'paru -S'
	done
}

install_community() {
	info_instalation "Installing community software"

	software=($(jq -r '.[] | select(.repository=="community") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

install_distro() {
	info_instalation "Installing distribution software"

	software=($(jq -r '.[] | select(.repository=="distro") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

install_extra() {
	info_instalation "Installing extra"

	software=($(jq -r '.[] | select(.repository=="extra") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		$name
	done
}

install_fonts() {
	info_instalation "Installing fonts"

	software=($(jq -r '.[] | select(.repository=="font") | .name' $software_root/software.json))
	cd $(xdg-user-dir DOWNLOAD)
	mkdir -p "$HOME/.local/share/fonts"
	for name in "${software[@]}"; do
		curl -LO "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.0/$name.zip"
		unzip $name.zip -d $HOME/.local/share/fonts/$name
	done
}

install_snap() {
	info_instalation "Installing snaps"

	software=($(jq -r '.[] | select(.repository=="snap") | .name' $software_root/software.json))
	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
	for name in "${software[@]}"; do
		install_package $name 'sudo snap install'
	done
}

install_total() {
	install_community
	install_distro
	install_aur
	install_snap
	install_extra
	install_fonts
}