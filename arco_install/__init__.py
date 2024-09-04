class RepositoryValues:
    """
    The class `RepositoryValues` defines lists of different types of repositories
    """
    DISTRO = ["distro", "community", "extra"]
    COMPILABLE = ["aur", "snap", "flatpack"]
    SCRIPT = ["script", "user"]
    ALL = DISTRO + COMPILABLE + SCRIPT


class SoftwareKeys:
    """
    The class `SoftwareKeys` defines constants for keys related to software information.
    """
    REPOSITORY = "Repository"
    NAME = "Name"
    TAGS = "Tags"
    SOFTWARE = "Software"


software_input  = "software/software.csv"
software_output = "software/software.yml"
sh_output       = "software/arco_install.sh"
log_output      = "arco_install.log"
