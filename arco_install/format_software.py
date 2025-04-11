from yaml import safe_load as safe
from arco_install import software_input, SoftwareKeys


def read_software() -> dict:
    data = safe(open(software_input, "r"))
    ns=[]
    for s,r in data[SoftwareKeys.SOFTWARE].items():
        ns.append({SoftwareKeys.NAME: s, SoftwareKeys.REPOSITORY: r})
    data[SoftwareKeys.SOFTWARE] = ns
    return data


read_installation_command = (
    lambda repository: read_software()
    .get(SoftwareKeys.REPOSITORY, {})
    .get(repository, {})
)

read_software_list = lambda repository: [
    software.get('Name')
    for software in read_software()[SoftwareKeys.SOFTWARE]
    if software[SoftwareKeys.REPOSITORY] == repository
]
