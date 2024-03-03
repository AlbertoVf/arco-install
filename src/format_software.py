from colorama import init, Fore, Style
import datetime, csv, yaml

init()

path = "./software/software"
date = datetime.datetime.now().strftime("%H:%M:%S")

log_date = lambda a: print(f"{Fore.BLUE + Style.BRIGHT}[{date}] {a}.{Style.RESET_ALL}")


def log_is_installed(software):
    msg = f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}"
    print(msg)
    return msg


def log_is_not_installed(software):
    msg = f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}"
    print(msg)
    return msg


def log_error_install(software, error):
    msg = f"{Fore.RED + Style.BRIGHT}[{date}] Error installing {software} - {error}"
    print(msg)
    return msg


def log(msg):
    with open("arco_install.log", "a") as f:
        f.write(f"{msg}\n")


def package_format():

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
        data = yaml.safe_load(open(json_file_path, "r"))
        data["software"] = read_from_csv()
        yaml.dump(data, open(json_file_path, "w"), default_flow_style=False)

    log_date("Software file updated")
    export_to_yaml()


def read_installation_command(repository):
    yaml_file_path = path + ".yml"

    with open(yaml_file_path, "r") as yaml_file:
        datos = yaml.safe_load(yaml_file)

    return datos["repository"][repository]  # Imprime el contenido del archivo YAML


def read_software_list(repository):
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
