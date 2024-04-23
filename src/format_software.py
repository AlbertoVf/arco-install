import datetime, csv, yaml, json
from .repository_values import SoftwareKeys
from .log import log_date
from .conf import (
    yml_software_output,
    software_file_data,
    yml_repository_input,
    json_software_output,
)

read_software_data = lambda: yaml.safe_load(open(yml_software_output, "r"))


# *
# * IMPORT FUNCTION
# *


def import_software_from_csv() -> list:
    """
    The function `import_software_from_csv` reads data from a CSV file and returns it as a list of dictionaries.

    Returns:
      A list of dictionaries containing the data imported from a CSV file.
    """
    data_csv = []
    with open(software_file_data, "r") as f:
        csv_reader = csv.DictReader(f, delimiter=";")
        for row in csv_reader:
            row = {key.strip(): value.strip() for key, value in row.items()}
            data_csv.append(row)
    return data_csv


@log_date("Read Software list")
def read_software_list() -> list:
    """
    The function `read_software_list` returns a list of software imported from a CSV file.

    Returns:
      A list of software items is being returned.
    """
    return import_software_from_csv()


# *
# * EXPORT FUNCTION
# *


@log_date("Export to YAML")
def export_to_yaml():
    """
    The function `export_to_yaml` reads data from a YAML file, updates it with software information, and
    then writes the updated data back to a YAML file.
    """
    yaml_file_path = yml_software_output
    data = yaml.safe_load(open(yml_repository_input, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)


@log_date("Export to JSON")
def export_to_json():
    """
    The function `export_to_json` reads data from a YAML file, adds a software list, and exports the
    data to a JSON file.
    """
    data = yaml.safe_load(open(yml_repository_input, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    json.dump(data, open(json_software_output, "w"))


@log_date("Software file updated")
def export_to_file():
    """
    The function `export_to_file` likely exports data to a file in YAML format.
    """
    export_to_yaml()
