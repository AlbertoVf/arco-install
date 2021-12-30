# Arco Install

Install software in your Arcolinux distribution

## Installation

- community: Software in the community repository
- aur: Include Aur packages
- snap: Software in the Snap store

```bash
# Update mirrorlist
sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist
# Update packages
sudo pacman -Sy
```

```bash
# Install software
sh install_software.sh
sh extra.sh
```

```bash
# Clone dotfiles
git clone --bare https://gitlab.com/AlbertoVf1/dotfiles $HOME/dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --working-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
```