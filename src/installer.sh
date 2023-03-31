source src/format-software.sh

function install_package(){
	name=$1
	if [ -z "$2"]; then
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

function update_packages() {
	info_instalation "Updating packages"
	sudo reflector --verbose -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist && sudo pacman -Syyu
	install_package "jq"
	format_software
}

function install_community() {
	info_instalation "Installing community software"

	software=($(jq -r '.[] | select(.repositorio=="community") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

function install_distro() {
	info_instalation "Installing distribution software"

	software=($(jq -r '.[] | select(.repositorio=="distro") | .paquete' $software_root/software.json))
	for name in "${software[@]}"; do
		install_package $name
	done
}

function install_aur() {
	info_instalation "Installing aur packages"

	dest="$(xdg-user-dir DOWNLOAD)/aur"
	software=($(jq -r '.[] | select(.repositorio=="aur") | .paquete' $software_root/software.json))
	mkdir $dest || cd $dest

	install_package 'git'
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

	software=($(jq -r '.[] | select(.repositorio=="snap") | .paquete' $software_root/software.json))
	install_package 'snapd'
	sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
	for name in "${snaps[@]}"; do
		install_package $name 'snap install'
	done
}

function install_extra() {
	info_instalation "Installing extra"

	software=($(jq -r '.[] | select(.repositorio=="extra") | .paquete' $software_root/software.json))
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

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
	install_package "jq"
	format_software
fi
