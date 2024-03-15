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


def console_log_message(software: str, status, error: str = "") -> str:
    """
    This Python function `console_log_message` logs messages related to software installation status and
    errors.

    :param software: The `software` parameter is a string that represents the name of the software
    package being processed in the function `console_log_message`
    :type software: str
    :param status: The `status` parameter in the `console_log_message` function represents the current
    status of the software package. It can have one of the following values:
    :param error: The `error` parameter in the `console_log_message` function is a string that
    represents any error message that occurred during the installation process of a software package. If
    the `status` parameter is set to "ERROR", this `error` message will be included in the log message
    that is printed out
    :type error: str
    :return: The function `console_log_message` returns the formatted log message based on the input
    parameters and then prints the message to the console.
    """
    msg = ""
    if status == "INSTALLED":
        msg = f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}"
    elif status == "NOT INSTALLED":
        msg = f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}"
    elif status == "ERROR":
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
