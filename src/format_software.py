import datetime, csv, yaml, json

from .repository_values import SoftwareKeys
from .log import log_date

path = "./software/software"
read_software_data = lambda: yaml.safe_load(open(path + ".yml", "r"))


# *
# * IMPORT FUNCTION
# *


def import_software_from_csv() -> list:
    csv_file_path = path + ".csv"
    data_csv = []
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            data_csv.append(row)
    return data_csv


@log_date("Read Software list")
def read_software_list() -> list:
    return import_software_from_csv()


# *
# * EXPORT FUNCTION
# *


@log_date("Export to YAML")
def export_to_yaml():
    yaml_file_path = path + ".yml"
    data = yaml.safe_load(open(f"{path}.bak.yml", "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)


@log_date("Export to JSON")
def export_to_json():
    json_file_path = path + ".json"
    data = json.load(open(json_file_path, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    json.dump(data, open(json_file_path, "w"))


@log_date("Software file updated")
def export_to_file():
    export_to_yaml()
