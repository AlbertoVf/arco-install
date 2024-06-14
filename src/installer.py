import subprocess
from .format_software import export_to_file, read_software_data as sd
from .log import log_date, log, console_log_message
from .repository_values import RepositoryValues, SoftwareKeys
from .conf import sh_export_script

read_installation_command = lambda repository: sd()[SoftwareKeys.REPOSITORY][repository]

read_software_list = lambda repository: [
    software
    for software in sd()[SoftwareKeys.SOFTWARE]
    if software[SoftwareKeys.REPOSITORY] == repository
]


@log_date("Updating packages")
def update():
    """
    The `update()` function runs the `reflector` command with specific options to update the mirrorlist for pacman package manager in Arch Linux
    ."""
    subprocess.run(
        "sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist",
        shell=True,
        check=True,
    )


def package_install(software: str, repository: str):
    """
    The function `package_install` checks if a software package is installed and installs it from a
    specified repository if it is not already installed.

    Args:
      software (str): The `software` parameter in the `package_install` function refers to the name of the software package that you want to install or check if it is already installed.
      repository (str): The `repository` parameter in the `package_install` function is expected to be a string that represents the repository from which the software package will be installed. It seems like the repository string is split by spaces to form a command for installation.
    """

    def is_installed(software):
        command = read_installation_command("check").split(" ") + [software]

        status = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return status.returncode == 0

    command = repository.split(" ") + [software]

    if is_installed(software):
        a = console_log_message(software, "INSTALLED")
    else:
        try:
            console_log_message(software, "NOT INSTALLED")
            subprocess.run(command, check=True)
            a = console_log_message(software, "INSTALLED")
        except subprocess.CalledProcessError as e:
            a = console_log_message(software, "ERROR", str(e))
    log(a)


def install(repository: str):
    """
    The `install` function installs packages from a specified repository using a given installation
    command and software list.

    Args:
      repository (str): The `repository` parameter is a string that represents the name or location of the software repository from which packages are to be installed.
    """
    log_date(f"Installing {repository} packages")
    command = read_installation_command(repository)
    software = read_software_list(repository)
    for s in software:
        package_install(s[SoftwareKeys.NAME], command)


def clear_cache():
    """
    The `clear_cache` function removes cached data using `paru` and `snapd` commands in Python.
    """
    subprocess.run(["paru", "-Scc"], check=True)
    subprocess.run(["rm", "-rf", "/var/cache/snapd/*"], check=True)


def export_scripts(repositories: list[RepositoryValues]):
    """
    The function `export_scripts` exports installation commands to a bash script based on a list of repositories.

    Args:
      repositories (list[RepositoryValues]): The `repositories` parameter is a list of `RepositoryValues` objects.
    """

    @log_date("Export to bash-script")
    def _export_scripts(repository: str):
        sf = []
        for s in software:
            if command != None:
                sf.append(f"{command} {s[SoftwareKeys.NAME]}\n")
            else:
                sf.append(f"{s[SoftwareKeys.NAME]}\n")
        return sf

    with open(sh_export_script, "w") as f:
        for repository in repositories:
            command = read_installation_command(repository)
            software = read_software_list(repository)
            f.writelines(_export_scripts(repository))
