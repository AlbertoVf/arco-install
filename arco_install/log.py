from colorama import init, Fore, Style
from datetime import datetime
from arco_install import log_output

init()

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log = lambda msg: open(log_output, "a").write(f"{date} {msg}\n")


def console_log_message(software: str, status: str, error: str = "") -> str:
    """
    Print with colors a terminal message with information about software
    """
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
            result = func(*args, **kwargs)
            print(f"{date} {msg}")
            return result
        return wrapper
    return decorator_function
