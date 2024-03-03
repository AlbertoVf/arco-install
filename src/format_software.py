from colorama import init, Fore, Style
import datetime, csv, yaml,json

init()

path = "./software/software"
date = datetime.datetime.now().strftime("%H:%M:%S")

log_date = lambda a: print(f"{Fore.BLUE + Style.BRIGHT}[{date}] {a}.{Style.RESET_ALL}")


def log_is_installed(software)->str:
    """
    The function `log_is_installed` logs a message indicating that a specified software package is
    already installed.

    :param software: The `software` parameter in the `log_is_installed` function represents the name of
    the software package that is being checked for installation
    :return: The function `log_is_installed` is returning the `msg` variable, which is a formatted
    string indicating that the package is already installed.
    """
    msg = f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}"
    print(msg)
    return msg


def log_is_not_installed(software)->str:
    """
    The function `log_is_not_installed` logs a message indicating that a software package is being
    installed.

    :param software: The `software` parameter in the `log_is_not_installed` function represents the name
    of the software package that is being installed
    :return: The function `log_is_not_installed` is returning the log message that is being printed to
    the console. The log message includes the installation information for the specified software
    package.
    """
    msg = f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}"
    print(msg)
    return msg


def log_error_install(software, error)->str:
    """
    The function `log_error_install` logs an error message when installing a software with the specified
    error.

    :param software: Software is a variable that represents the name of the software that encountered an
    error during installation
    :param error: The `error` parameter in the `log_error_install` function is used to specify the error
    message that occurred during the installation of the software. This error message will be included
    in the log message that is printed out by the function
    :return: The function `log_error_install` is returning the formatted error message `msg`.
    """
    msg = f"{Fore.RED + Style.BRIGHT}[{date}] Error installing {software} - {error}"
    print(msg)
    return msg


def log(msg):
    """
    The `log` function appends a message to a log file named "arco_install.log".

    :param msg: The `msg` parameter in the `log` function is a string that represents the message or
    information that you want to log into the "arco_install.log" file
    """
    with open("arco_install.log", "a") as f:
        f.write(f"{msg}\n")


def package_format():
    """
    The `package_format` function reads data from a CSV file, updates a YAML file with the data, and
    logs the update.
    """

    def read_from_csv():
        csv_file_path = path + ".csv"
        data_csv = []
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            for row in csv_reader:
                data_csv.append(row)
        return data_csv

    def export_to_yaml():
        yaml_file_path = path + ".yml"
        data = yaml.safe_load(open(yaml_file_path, "r"))
        data["software"] = read_from_csv()
        yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)

    def export_to_json():
        json_file_path = path + ".json"
        data = json.load(open(json_file_path, "r"))
        data["software"] = read_from_csv()
        json.dump(data, open(json_file_path, "w"))

    log_date("Software file updated")
    export_to_yaml()


def read_installation_command(repository):
    """
    The function reads an installation command from a YAML file based on a given repository.

    :param repository: The `repository` parameter in the `read_installation_command` function is used to
    specify which installation command to read from the YAML file. The function reads the YAML file
    specified by `yaml_file_path` and returns the installation command associated with the given
    `repository` key in the YAML data
    :return: The function `read_installation_command` reads a YAML file specified by `repository` and
    returns the installation command for that repository as specified in the YAML file.
    """
    yaml_file_path = path + ".yml"

    with open(yaml_file_path, "r") as yaml_file:
        datos = yaml.safe_load(yaml_file)

    return datos["repository"][repository]  # Imprime el contenido del archivo YAML


def read_software_list(repository):
    """
    The function `read_software_list` reads a YAML file containing software information and returns a
    list of software entries based on a specified repository.

    :param repository: The `repository` parameter in the `read_software_list` function is used to filter
    the list of software based on the specified repository. The function reads a YAML file containing
    software information, extracts the software list, and then filters it based on the provided
    repository value. The filtered list of software that
    :return: The function `read_software_list(repository)` returns a list of software items from a YAML
    file that match the specified repository.
    """
    yaml_file_path = path + ".yml"

    with open(yaml_file_path, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    software = [
        software
        for software in data["software"]
        if software["repository"] == repository
    ]

    return software


if __name__ == "__main__":
    package_format()
