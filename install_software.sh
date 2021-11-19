#!/bin/bash

info_instalation() {
  tput setaf 5; printf "\n[ $(date) ]  $1\n"; tput sgr0
}

is_installed() {
  tput setaf 2; printf "\n[ $(date) ]  The package $1 is already installed\n"; tput sgr0
}
is_not_installed() {
  tput setaf 3; printf "\n[ $(date) ]  Installing package $1\n"; tput sgr0
}

install_community() {
  info_instalation "Installing community.list"; software=($(cat community.list))
  for name in "${software[@]}" ; do
    if pacman -Qi $name &> /dev/null; then
      is_installed $name
    else
      is_not_installed $name
      sudo pacman -Sy --noconfirm --needed $name
    fi
  done
}

install_fonts() {
  info_instalation "Installing fonts.list"; fonts=($(cat fonts.list))
  for name in "${fonts[@]}"; do
    if pacman -Qi $name &> /dev/null; then
      is_installed $name
    else
      is_not_installed $name;paru $name
    fi
  done
}

install_snap() {
  info_instalation "Installing snap.list"; snaps=($(cat snaps.list))
  sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap
  for name in "${snaps[@]}" ; do
    if pacman -Qi $name &> /dev/null; then
      is_installed $name
    else
      is_not_installed $name;sudo snap install $name
    fi
  done
}

install_aur() {
  info_instalation "Installing aur.list"; aur=($(cat aur.list))
  mkdir ~/.cache/paru/clone
  for name in "${aur[@]}" ; do
    cd ~/.cache/paru/clone || exit;
    if pacman -Qi $name &> /dev/null; then
      is_installed $name
    else
      is_not_installed $name
      git clone https://aur.archlinux.org/$name.git && cd $name && makepkg -si --needed --noconfirm
    fi
  done
}

install_lang() {
  info_instalation "Installing lang.list"; lang=($(cat lang.list))
  for name in "${lang[@]}" ; do
    if pacman -Qi $name &> /dev/null; then
      is_installed $name
    else
      is_not_installed $name
      sudo pacman -Sy --noconfirm --needed $name
    fi
  done
}