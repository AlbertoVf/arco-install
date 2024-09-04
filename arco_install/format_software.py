import datetime, csv
from yaml import safe_load as safe, dump
from arco_install.log import log_date
from arco_install import software_output, software_input, SoftwareKeys

read_software_data = lambda: safe(open(software_output, "r"))


@log_date("Read Software list")
def read_software_list() -> list:
    """
    Read software data from from csv and save
    """
    data_csv = []
    with open(software_input, "r") as f:
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
    Build software file from `read_software_list()`
    """
    data = safe(open(software_output, "r"))
    data[SoftwareKeys.SOFTWARE] = read_software_list()
    dump(data, open(software_output, "w"), default_flow_style=False)
