# Arco Install

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT) [![GitHub](https://img.shields.io/github/tag/AlbertoVf/arco-install.svg?style=flat-square)](https://github.com/AlbertoVf/arco-install/tags)

Instalador de software en [Arcolinux](https://arcolinux.com/).

Este repositorio contiene un script de instalación para ArcoLinux, una distribución de Linux basada en Arch Linux. Con este script, puedes instalar software en ArcoLinux fácilmente y personalizar tu instalación.

## Tipo de software

- `minimal`: software básico
- `terminal`: software de comandos de terminal
- `gammer`: software para juegos
- `programing`: software para programación
- `all`: todo tipo de software

## Tipos de repositorios

- `community`: software de la comunidad
- `distro`: software propio de la distribución
- `aur`: software de usuarios para [archlinux](https://aur.archlinux.org/)
- `snap`: software [snap](https://snapcraft.io/store)
- `extra`: software/configuraciones instalado a traves de comandos


## Ejecución

```sh
# Crea un fichero json a partir del archivo csv
sh src/format-software.sh
```

```sh
# ejecuta el script de instalación
sudo sh arco-install.sh
```
