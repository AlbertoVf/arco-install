# Arco Install

[![The MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](http://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/github/tag/AlbertoVf/arco-install.svg?style=for-the-badge)](https://github.com/AlbertoVf/arco-install/tags)

Software installer to [Arcolinux](https://arcolinux.com/).

## Software Data

> [!IMPORTANT]
> Configure filepath on `arco_install/__init__.py`
> Rename `software.template.yml` to `software.yml` OR replace `software_input`

### Input file

The default software is a yaml file with `Repository` and `Software`

- `Repository`: repository name and command installation software
- `Software`:: list of software with `package_name`: `repository_name`

![software csv](docs/software_format.png)

## Command line usage

![Use diagram](docs/use_diagram.drawio.svg)

- Run help command

    ```bash
    python arco_install.py -h
    ```

    ```log
    usage: arco_install.py [-h] [-a] [-c] [-d] [-s] [-e]

    Install the required packages

    options:
    -h, --help        show this help message and exit
    -a, --all         Install all software
    -c, --compilable  Install software from AUR, snap
    -d, --distro      Install software from distribution and communnity
    -s, --script      Install extra software
    -e, --export      Build bashscript installation file
    ```

- Install script command: Run scripts who is a command line, not a package

    ```bash
    python arco_install.py [-s | --script]
    ```

- Install all software included in the software file

    ```bash
    python arco_install.py [-a | --all]
    ```

- Install software included in repositories who necessary compilation: snap, aur, flatpack...

    ```bash
    python arco_install.py [-c | --compilable]
    ```

- Install software included in the distribution repositories: community, distribution, extra, large_support, 3rd_...

    ```bash
    python arco_install.py [-d | --distro]
    ```

- Build a `.sh` file to install any software manually ( 1 line = 1 command installation)

    ```bash
    python arco_install.py [-e | --export]
    ```
