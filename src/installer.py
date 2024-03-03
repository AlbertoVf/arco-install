import subprocess
from .format_software import (
    log_is_not_installed,
    log_is_installed,
    log_date,
    log_error_install,
    read_installation_command,
    read_software_list,
    package_format,
    log
)


def update():
    log_date("Updating packages")
    subprocess.run(
        "sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist",
        shell=True,
        check=True,
    )


def install_necessary():
    for s in ["git", "paru", "snapd"]:
        package_install(s, read_installation_command("distro"))
    package_format()
    subprocess.run(
        "sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap",
        shell=True,
        check=True,
    )


def package_install(software, repository: str):
    def is_installed(software):
        command = read_installation_command("check").split(" ") + [software]

        status = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return status.returncode == 0

    command = repository.split(" ") + [software]

    if is_installed(software):
        a = log_is_installed(software)
    else:
        try:
            log_is_not_installed(software)
            subprocess.run(command, check=True)
            a = log_is_installed(software)
        except subprocess.CalledProcessError as e:
            a = log_error_install(software, str(e))

    log(a)


def install(repository):
    log_date(f"Installing {repository} packages")
    command = read_installation_command(repository)
    software = read_software_list(repository)
    for s in software:
        package_install(s["name"], command)
