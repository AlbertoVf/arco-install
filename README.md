# Arco Install

Install software in your Arcolinux distribution

## Installation

- community: Software in the community repository
- aur: Include Aur packages
- snap: Software in the Snap store

```bash
# run as superuser
sudo python main.py
```

```bash
# Clone dotfiles
git clone --bare https://gitlab.com/AlbertoVf1/dotfiles $HOME/dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --working-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
```
