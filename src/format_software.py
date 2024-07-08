import datetime, csv
from yaml import safe_load, dump
from .log import log_date
from .repository_values import (
    software_output,
    software_file_data,
    repository_input,
    SoftwareKeys,
)

read_software_data = lambda: safe_load(open(software_output, "r"))


@log_date("Read Software list")
def read_software_list() -> list:
    """
    The function `read_software_list` returns a list of software imported from a CSV file.

    Returns:
      A list of software items is being returned.
    """
    data_csv = []
    with open(software_file_data, "r") as f:
        csv_reader = csv.DictReader(f, delimiter=";")
        for row in csv_reader:
            row = {
                key.strip(): value.strip()
                for key, value in row.items()
                if key != "Tags"
            }
            data_csv.append(row)
    return data_csv


@log_date("Software file updated")
def export_to_file():
    """
    The function `export_to_file` reads data from a YAML file, updates it with software information, and
    then writes the updated data back to a YAML file.
    """
    yaml_file_path = software_output
    data = safe_load(open(repository_input, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    dump(data, open(yaml_file_path, "w"), default_flow_style=True)
