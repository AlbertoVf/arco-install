#!/bin/sh
source src/format-software.sh

package::install() {
	name=$1
	if [ -z "$2" ]; then
		command="sudo pacman -Sy --noconfirm --needed"
	else
		command=$2
	fi

	if pacman -Qi $name &>/dev/null; then
		log::isInstalled $name | tee -a $log
	else
		log::isNotInstalled $name | tee -a $log
		$command $name 2>> $log
	fi
}

install::necessary() {
	package::install 'jq' # use to create json file
	package::install 'git' # use to download aur install
	package::install 'paru' # use to download aur install
	package::install 'unzip' # use to decompress zip files
	package::install 'snapd' # use to install snap install
	package::install 'curl' # use to download from url
	format_software
}

install::update() {
	log::date "Updating packages"
	sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Syyu
}

install::aur() {
	log::date "Installing aur packages"

	software=($(jq -r '.[] | select(.repository=="aur") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		package::install $name 'paru -S'
	done
}

install::community() {
	log::date "Installing community packages"

	software=($(jq -r '.[] | select(.repository=="community") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		package::install $name
	done
}

install::distro() {
	log::date "Installing distribution packages"

	software=($(jq -r '.[] | select(.repository=="distro") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		package::install $name
	done
}

install::extra() {
	log::date "Installing extra packages"

	software=($(jq -r '.[] | select(.repository=="extra") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		$name
	done
}

install::fonts() {
	log::date "Installing fonts packages"

	software=($(jq -r '.[] | select(.repository=="font") | .name' $software_root/software.json))
	cd $(xdg-user-dir DOWNLOAD)
	mkdir -p "$HOME/.local/share/fonts"
	for name in "${software[@]}"; do
		curl -LO "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.0/$name.zip"
		unzip $name.zip -d $HOME/.local/share/fonts/$name
	done
}

install::snap() {
	log::date "Installing snaps packages"

	software=($(jq -r '.[] | select(.repository=="snap") | .name' $software_root/software.json))
	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
	for name in "${software[@]}"; do
		package::install $name 'sudo snap install'
	done
}

install_total() {
	install::community
	install::distro
	install::aur
	install::snap
	install::extra
	install::fonts
}