class RepositoryValues:
    """
    The class `RepositoryValues` defines lists of different types of repositories
    """

    DISTRO     = ["distro", "community", "extra"]
    COMPILABLE = ["aur", "snap", "flatpack"]
    SCRIPT     = ["script", "user", "python"]
    ALL        = DISTRO + COMPILABLE + SCRIPT


class SoftwareKeys:
    """
    The class `SoftwareKeys` defines constants for keys related to software information.
    """

    REPOSITORY = "Repository"
    NAME       = "Name"
    TAGS       = "Tags"
    SOFTWARE   = "Software"
    DELIMITER  = ";"


software_input  = "software/software.csv"
software_output = "software/software.yml"
software_temp   = "software/software.template.yml"
sh_output       = "software/zarco_install.sh"
log_output      = "arco_install.log"


log = lambda msg: open(log_output, "a").write(f"{date} {msg}\n")


def date():
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
