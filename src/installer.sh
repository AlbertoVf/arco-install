#!/usr/bin/env sh
source src/format-software.sh

packageInstall() {
	name=$1
	if [ -z "$2" ]; then
		command="sudo pacman -Sy --noconfirm --needed"
	else
		command=$2
	fi

	if pacman -Qi $name &>/dev/null; then
		logIsInstalled $name | tee -a $log
	else
		logIsNotInstalled $name | tee -a $log
		$command $name 2>> $log
	fi
}

installNecessary() {
	packageInstall 'jq' # use to create json file
	packageInstall 'git' # use to download aur install
	packageInstall 'paru' # use to download aur install
	packageInstall 'unzip' # use to decompress zip files
	packageInstall 'snapd' # use to install snap install
	packageInstall 'curl' # use to download from url
	formatSoftware
}

installUpdate() {
	logDate "Updating packages"
	sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Syyu
}

installAur() {
	logDate "Installing aur packages"

	software=($(jq -r '.[] | select(.repository=="aur") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		packageInstall $name 'paru -S'
	done
}

installCommunity() {
	logDate "Installing community packages"

	software=($(jq -r '.[] | select(.repository=="community") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		packageInstall $name
	done
}

installDistro() {
	logDate "Installing distribution packages"

	software=($(jq -r '.[] | select(.repository=="distro") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		packageInstall $name
	done
}

installExtra() {
	logDate "Installing extra packages"

	software=($(jq -r '.[] | select(.repository=="extra") | .name' $software_root/software.json))
	for name in "${software[@]}"; do
		$name
	done
}

installFonts() {
	logDate "Installing fonts packages"

	software=($(jq -r '.[] | select(.repository=="font") | .name' $software_root/software.json))
	cd $(xdg-user-dir DOWNLOAD)
	mkdir -p "$HOME/.local/share/fonts"
	for name in "${software[@]}"; do
		curl -LO "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.0/$name.zip"
		unzip $name.zip -d $HOME/.local/share/fonts/$name
	done
}

installSnap() {
	logDate "Installing snaps packages"

	software=($(jq -r '.[] | select(.repository=="snap") | .name' $software_root/software.json))
	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
	for name in "${software[@]}"; do
		packageInstall $name 'sudo snap install'
	done
}

installTotal() {
	installCommunity
	installDistro
	installAur
	installSnap
	installExtra
	installFonts
}