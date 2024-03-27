class RepositoryValues:
    """
    The class `RepositoryValues` defines lists of different types of repositories who use the same installation command
    """

    DISTRO = ["distro", "community", "extra"]
    COMPILABLE = ["aur", "snap", "flatpack"]
    SCRIPT = ["script"]
    ALL = DISTRO + COMPILABLE + SCRIPT


class SoftwareKeys:
    """
    The class `SoftwareKeys` defines constants for keys related to software information.
    """

    REPOSITORY = "Repository"
    NAME = "Name"
    TAGS = "Tags"
    SOFTWARE = "Software"
