source src/format-software.sh
source src/check.sh

format_software

function install_community() {
	info_instalation "Installing community software"
	software=($(jq '.[] | select(.repositorio=="community") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		if pacman -Qi $name &>/dev/null; then
			is_installed $name
		else
			is_not_installed $name
			sudo pacman -Sy --noconfirm --needed $name
		fi
	done
}

function install_distro() {
	info_instalation "Installing distribution software"
	software=($(jq '.[] | select(.repositorio=="distro") | .paquete' $software_root/software.json))

	for name in "${software[@]}"; do
		if pacman -Qi $name &>/dev/null; then
			is_installed $name
		else
			is_not_installed $name
			sudo pacman -Sy --noconfirm --needed $name
		fi
	done
}

function install_aur() {
	dest="$(xdg-user-dir DOWNLOAD)/aur"
	info_instalation "Installing aur packages"
	software=($(jq '.[] | select(.repositorio=="aur") | .paquete' $software_root/software.json))

	mkdir $dest || cd $dest
	for name in "${aur[@]}"; do
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

function install_snap() {
	info_instalation "Installing snaps"
	software=($(jq '.[] | select(.repositorio=="snap") | .paquete' $software_root/software.json))

	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
	for name in "${snaps[@]}"; do
		if pacman -Qi $name &>/dev/null; then
			is_installed $name
		else
			is_not_installed $name
			sudo snap install $name
		fi
	done
}

function install_extra() {
	echo "Installing extra"
	software=($(jq '.[] | select(.repositorio=="extra") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		$name
	done
}

function install_all() {
	install_community
	install_distro
	install_aur
	install_snap
	install_extra
}