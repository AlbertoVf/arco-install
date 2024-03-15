import subprocess
from .format_software import (
    SoftwareKeys,
    log_date,
    log_is_not_installed,
    log_is_installed,
    log_error_install,
    package_format,
    log,
    import_file_as_dict,
)

software_data = import_file_as_dict()

read_installation_command = lambda repository: software_data[SoftwareKeys.REPOSITORY][
    repository
]

read_software_list = lambda repository: [
    software
    for software in software_data[SoftwareKeys.SOFTWARE]
    if software[SoftwareKeys.REPOSITORY] == repository
]


def update():
    """
    The `update()` function runs the `reflector` command to update package mirrors for the Pacman
    package manager in Arch Linux.
    """
    log_date("Updating packages")
    subprocess.run(
        "sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist",
        shell=True,
        check=True,
    )


def install_necessary():
    """
    The function `install_necessary` installs necessary packages, formats packages, and enables snapd
    socket.
    """
    for s in ["git", "paru", "snapd"]:
        package_install(s, read_installation_command("distro"))
    package_format()
    subprocess.run(
        "sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap",
        shell=True,
        check=True,
    )


def package_install(software, repository: str):
    """
    The function `package_install` checks if a software package is installed, installs it if not, and
    logs the installation status.

    :param software: The `software` parameter in the `package_install` function refers to the name of
    the software package that you want to install or check for installation status. It is a string
    representing the name of the software package
    :param repository: The `repository` parameter in the `package_install` function is expected to be a
    string that represents the repository from which the software package will be installed. This string
    is then split into a list of elements using the space character as the delimiter
    :type repository: str
    """

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
    """
    The `install` function installs packages from a specified repository using a given installation
    command.

    :param repository: It looks like you were about to provide some information about the `repository`
    parameter, but it seems to have been cut off. Could you please provide more details or let me know
    how I can assist you further with the `repository` parameter?
    """
    log_date(f"Installing {repository} packages")
    command = read_installation_command(repository)
    software = read_software_list(repository)
    for s in software:
        package_install(s[SoftwareKeys.NAME], command)


def clear_cache():
    subprocess.run(["paru", "-Scc"], check=True)
    subprocess.run(["rm", "-rf", "/var/cache/snapd/*"], check=True)


def export_scripts(repository):
    command = read_installation_command(repository)
    software = read_software_list(repository)
    with open ('arco_install.sh','w') as f:
        for s in software:
            f.write(f"{command} {s[SoftwareKeys.NAME]}\n")
