from dotenv import load_dotenv
from os import getenv as env

load_dotenv()


class RepositoryValues:
    DISTRO = ["distro", "community", "extra"]
    COMPILABLE = ["aur", "snap", "flatpack"]
    SCRIPT = ["script", "user"]
    ALL = DISTRO + COMPILABLE + SCRIPT


class SoftwareKeys:
    REPOSITORY = "Repository"
    NAME = "Name"
    TAGS = "Tags"
    SOFTWARE = "Software"


software_file_data = env("SOFTWARE_CSV")
repository_input = env("BAK_FILE")
software_output = env("EXPORT_YML")
json_software_output = env("EXPORT_JSON")
sh_export_script = env("EXPORT_SCRIPT")
log_output = env("LOG")
