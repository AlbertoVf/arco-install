import datetime, csv, yaml, json
from .repository_values import SoftwareKeys
from .log import log_date
from .conf import yml_software_output, software_file_data, yml_repository_input, json_software_output

read_software_data = lambda: yaml.safe_load(open(yml_software_output, "r"))


# *
# * IMPORT FUNCTION
# *


def import_software_from_csv() -> list:
    data_csv = []
    with open(software_file_data, "r") as f:
        csv_reader = csv.DictReader(f, delimiter=";")
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
    yaml_file_path = yml_software_output
    data = yaml.safe_load(open(yml_repository_input, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)


@log_date("Export to JSON")
def export_to_json():
    data = yaml.safe_load(open(yml_repository_input, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    json.dump(data, open(json_software_output, "w"))


@log_date("Software file updated")
def export_to_file():
    export_to_yaml()
