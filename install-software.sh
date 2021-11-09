#!/bin/bash
func_install() {
  # Author : Erik Dubois
  if pacman -Qi $1 &> /dev/null; then
    tput setaf 2
    printf "\n[ $(date) ]  The package $1 is already installed\n"
    tput sgr0
  else
    tput setaf 3
    printf "\n[ $(date) ]  Installing package $1\n"
    tput sgr0
    sudo pacman -Sy --noconfirm --needed $1
  fi
}

info_instalation() {
  tput setaf 5
  printf "\n[ $(date) ]  $1\n"
  tput sgr0
}

install_community() {
  info_instalation "Installing community.list"
  software=($(cat community.list))
  for name in "${software[@]}" ; do
    func_install $name
  done
}

install_fonts() {
  info_instalation "Installing fonts.list"
  fonts=($(cat fonts.list))
  for name in "${fonts[@]}"; do
    info_instalation "Installing font: $name ";paru $name
  done
}

install_snap() {
  info_instalation "Installing snap.list"
  sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
  snaps=($(cat snaps.list))
  for name in "${snaps[@]}" ; do
    info_instalation "Installing snap: $name ";sudo snap install $name
  done
}

install_aur() {
  info_instalation "Installing aur.list"
  aur=($(cat aur.list))
  mkdir ~/.cache/paru/clone
  for name in "${aur[@]}" ; do
    cd ~/.cache/paru/clone || exit;
    info_instalation "Installing aur: $name ";
    git clone https://aur.archlinux.org/$name.git
    cd $name && makepkg -si --needed --noconfirm;
  done
}

install_lang() {
  info_instalation "Installing lang.list"
  lang=($(cat lang.list))
  for name in "${lang[@]}" ; do
    info_instalation "Installing language: $name "
    func_install $name
  done
}
