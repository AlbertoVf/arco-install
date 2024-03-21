# Arco Install

[![The MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](http://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/github/tag/AlbertoVf/arco-install.svg?style=for-the-badge)](https://github.com/AlbertoVf/arco-install/tags)

Software installer to [Arcolinux](https://arcolinux.com/).

## Software

## Instalation scripts

```yaml
repository:
  aur: sudo paru -S
  check: sudo pacman -Qq
  community: sudo pacman -Sy --noconfirm --needed
  distro: sudo pacman -Sy --noconfirm --needed
  extra: sudo pacman -Sy --noconfirm --needed
  script: sudo
  snap: sudo snap install
```

## Yaml software format

```yaml
- Name: archlinux-betterlockscreen
  Repository: distro
  Tags: theme
```

## Software File

```yaml
repository:
    ...
software:
    ...
```

## Running

```txt
📂
├── 📂 software
│  ├── 📜 software.csv
│  └── 📜 software.yml
└── 📂 src
|   ├── 🐚 format-software.py
|   └── 🐚 installer.py
└── 🐚 arco_install.py
```

```python
# [!TIP] Use to only build software.yml
python src/format_software.py
```

```python
# Run instalation script
sudo python arco_install.py
```

![Use diagram](./docs/use_diagram.svg)
