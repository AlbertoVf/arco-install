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


software_input = "software/software.yml"
sh_output       = "software/arco_install.sh"
log = lambda msg: open("arco_install.log", "a").write(f"{date} {msg}\n")


def date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def console_log_message(software: str, status: str, error: str = "") -> str:
    """
    Print with colors a terminal message with information about software
    """

    from colorama import init, Fore, Style

    init()

    STATUS = {
        "INSTALLED": f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}",
        "NOT INSTALLED": f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}",
        "ERROR": f"{Fore.RED + Style.BRIGHT}[{date}] Error installing {software} - {error}",
    }
    msg = STATUS[status]
    print(msg)


def log_date(msg: str):
    """
    Decorator to print date and message
    """
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            print(f"{date()} {msg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator_function
