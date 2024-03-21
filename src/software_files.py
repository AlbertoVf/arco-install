import csv, yaml, json
from .log import console_extra_log
from .repository_values import SoftwareKeys


@console_extra_log("Import software from data")
def import_software_from_csv():
    csv_file_path = path + ".csv"
    data_csv = []
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            data_csv.append(row)
    return data_csv


@console_extra_log("Export software to YAML")
def export_to_yaml():
    yaml_file_path = path + ".yml"
    data = yaml.safe_load(open(f"{path}.bak.yml", "r"))
    data[SoftwareKeys.SOFTWARE] = import_software()
    yaml.dump(data, open(yaml_file_path, "w"), default_flow_style=False)


@console_extra_log("Export software to JSON")
def export_to_json():
    json_file_path = path + ".json"
    data = json.load(open(json_file_path, "r"))
    data[SoftwareKeys.SOFTWARE] = import_software()
    json.dump(data, open(json_file_path, "w"))


def import_file_as_dict():
    return yaml.safe_load(open(path + ".yml", "r"))


path = "./software/software"
import_software = lambda: import_software_from_csv()
export_software = lambda: export_to_yaml()
