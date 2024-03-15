from colorama import init, Fore, Style
import datetime, csv, yaml, json

init()

path = "./software/software"
date = datetime.datetime.now().strftime("%H:%M:%S")
log_date = lambda a: print(f"{Fore.BLUE + Style.BRIGHT}[{date}] {a}.{Style.RESET_ALL}")
import_file_as_dict = lambda: yaml.safe_load(open(path + ".yml", "r"))
log = lambda msg: open("arco_install.log", "a").write(f"{msg}\n")


# The class `SoftwareKeys` defines constants for keys related to software information.
class SoftwareKeys:
    REPOSITORY = "Repository"
    NAME = "Name"
    TAGS = "Tags"
    SOFTWARE = "Software"


def log_is_installed(software) -> str:
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


def log_is_not_installed(software) -> str:
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


def log_error_install(software, error) -> str:
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
        data = yaml.safe_load(open(f"{path}.bak.yml", "r"))
        data[SoftwareKeys.SOFTWARE] = read_from_csv()
        yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)

    def export_to_json():
        json_file_path = path + ".json"
        data = json.load(open(json_file_path, "r"))
        data[SoftwareKeys.SOFTWARE] = read_from_csv()
        json.dump(data, open(json_file_path, "w"))

    log_date("Software file updated")
    export_to_yaml()


if __name__ == "__main__":
    package_format()
