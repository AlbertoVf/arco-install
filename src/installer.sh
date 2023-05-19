#!/bin/sh
source src/format-software.sh

install_package() {
	name=$1
	if [ -z "$2" ]; then
		command="pacman -Sy --noconfirm --needed"
	else
		command=$2
	fi

	if pacman -Qi $name &>/dev/null; then
		is_installed $name
	else
		is_not_installed $name
		sudo $command $name
	fi
}

install_necessary_packages() {
	install_package 'jq' # use to create json file
	install_package 'git' # use to download aur packages
	install_package 'unzip' # use to decompress zip files
	install_package 'snapd' # use to install snap packages
	install_package 'curl' # use to download from url
	format_software
}

update_packages() {
	info_instalation "Updating packages"
	sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Syyu
}

install_community() {
	info_instalation "Installing community software"

	software=($(jq -r '.[] | select(.repositorio=="community") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

install_distro() {
	info_instalation "Installing distribution software"

	software=($(jq -r '.[] | select(.repositorio=="distro") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

install_aur() {
	info_instalation "Installing aur packages"

	dest="$(xdg-user-dir DOWNLOAD)/aur"
	software=($(jq -r '.[] | select(.repositorio=="aur") | .paquete' $software_root/software.json))
	mkdir -p $dest || cd $dest

	for name in "${software[@]}"; do
		cd $dest || exit
		if pacman -Qi $name &>/dev/null; then
			is_installed $name
		else
			is_not_installed $name
			git clone https://aur.archlinux.org/$name.git
			cd $name && makepkg -si --needed --noconfirm
		fi
	done
}

install_snap() {
	info_instalation "Installing snaps"

	software=($(jq -r '.[] | select(.repositorio=="snap") | .paquete' $software_root/software.json))
	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap

	for name in "${software[@]}"; do
		install_package $name 'snap install'
	done
}

install_extra() {
	info_instalation "Installing extra"

	software=($(jq -r '.[] | select(.repositorio=="extra") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		$name
	done
}

install_fonts() {
	info_instalation "Installing fonts"

	software=($(jq -r '.[] | select(.repositorio=="font") | .paquete' $software_root/software.json))
	cd $(xdg-user-dir DOWNLOAD)

	for name in "${software[@]}"; do
		curl -LO "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.0/$name.zip"
		unzip $name.zip -d $HOME/.local/share/fonts/$name
	done
}

install_all() {
	install_community
	install_distro
	install_aur
	install_snap
	install_extra
	install_fonts
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
	format_software
fi
