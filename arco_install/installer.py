import subprocess
from arco_install.format_software import read_installation_command, read_software_list
from arco_install import RepositoryValues, sh_output, log, log_date, console_log_message


@log_date("update mirrorlist with reflector")
def update():
    subprocess.run( "sudo reflector -f 20 -l 15 -n 10 --save /etc/pacman.d/mirrorlist", shell=True, check=True, )


@log_date("Install the software")
def install(repository: str):

    def package_install(software: str, repository: str):
        def is_installed(software):
            command = read_installation_command("check").split(" ") + [software]
            status = subprocess.run( command, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            return status.returncode == 0

        command = repository.split(" ") + [software]

        if is_installed(software):
            console_log_message(software, "INSTALLED")
            log(f"WARNING: The package {software} was already installed")
        else:
            try:
                console_log_message(software, "NOT INSTALLED")
                subprocess.run(command, check=True)
                log(f"INFO: The package {software} has been installed correctly")
            except subprocess.CalledProcessError as e:
                console_log_message(software, "ERROR")
                log( f"ERROR: The package {software} could not be installed :: `{repository} {software}`" )

    log_date(f"Installing {repository} packages")
    command = read_installation_command(repository)
    software = read_software_list(repository)
    for s in software:
        package_install(s, command)


@log_date("Clear cache")
def clear_cache():
    subprocess.run(["paru", "-Scc"], check=True)
    subprocess.run(["rm", "-rf", "/var/cache/snapd/*"], check=True)


@log_date("Build sh file to run by terminal")
def export_scripts(repositories: list[RepositoryValues]):
    def _export_scripts():
        sf = []
        for s in software:
            sf.append(f"{command} {s}\n" if command != None else f"{s}\n")
        return sf

    with open(sh_output, "w") as f:
        for repository in repositories:
            command = read_installation_command(repository)
            software = read_software_list(repository)
            f.writelines(_export_scripts())
