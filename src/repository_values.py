# The class `RepositoryValues` defines lists of different types of repositories who use the same installation command
class RepositoryValues:
    DISTRO = ["distro", "community", "extra"]
    COMPILABLE = ["aur", "snap", "flatpack"]
    SCRIPT = ["script"]
    ALL = DISTRO + COMPILABLE + SCRIPT


# The class `SoftwareKeys` defines constants for keys related to software information.
class SoftwareKeys:
    REPOSITORY = "Repository"
    NAME = "Name"
    TAGS = "Tags"
    SOFTWARE = "Software"
