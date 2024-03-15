from colorama import init, Fore, Style
from datetime import datetime

init()

date = datetime.now().strftime("%H:%M:%S")
log = lambda msg: open("arco_install.log", "a").write(f"{msg}\n")


def console_log_message(software: str, status, error: str = "") -> str:
    STATUS = {
        "INSTALLED": f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}",
        "NOT INSTALLED": f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}",
        "ERROR": f"{Fore.RED + Style.BRIGHT}[{date}] Error installing {software} - {error}",
    }
    msg = STATUS[status]
    print(msg)
    return msg


def console_extra_log(msg):
    def decorator_funcion(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(msg)
            return result

        return wrapper

    return decorator_funcion


def log_date(msg):
    def decorator_funcion(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{Fore.BLUE + Style.BRIGHT}[{date}] {msg}.{Style.RESET_ALL}")
            return result

        return wrapper

    return decorator_funcion
