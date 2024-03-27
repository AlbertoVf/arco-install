from dotenv import load_dotenv
from os import getenv as env

load_dotenv()
software_file_data = env("SOFTWARE_CSV")
yml_repository_input = env("BAK_FILE")
yml_software_output = env("EXPORT_YML")
json_software_output = env("EXPORT_JSON")
sh_export_script = env("EXPORT_SCRIPT")
log_output = env("LOG")
