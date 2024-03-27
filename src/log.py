from colorama import init, Fore, Style
from datetime import datetime
from .conf import sh_export_script

init()

date = datetime.now().strftime("%H:%M:%S")
log = lambda msg: open(sh_export_script, "a").write(f"{msg}\n")


def console_log_message(software: str, status: str, error: str = "") -> str:
    """
    The function `console_log_message` logs messages related to software installation status and errors.

    Args:
      software (str): The `software` parameter is a string that represents the name of the software package being processed in the function `console_log_message`.
      status (str): The `status` parameter in the `console_log_message` function is used to determine the type of message to be logged. It can have one of the following values:
      error (str): The `error` parameter in the `console_log_message` function is used to specify the error message that occurred during the installation process if the status is "ERROR". This error message will be included in the log message that is printed out when the function is called with the "ERROR" status.

    Returns:
      The function `console_log_message` returns the log message based on the provided software status and error (if any).
    """
    STATUS = {
        "INSTALLED": f"{Fore.GREEN + Style.BRIGHT}[{date}] The package {software} is already installed.{Style.RESET_ALL}",
        "NOT INSTALLED": f"{Fore.YELLOW + Style.BRIGHT}[{date}] Installing package {software}.{Style.RESET_ALL}",
        "ERROR": f"{Fore.RED + Style.BRIGHT}[{date}] Error installing {software} - {error}",
    }
    msg = STATUS[status]
    print(msg)
    return msg


def console_extra_log(msg: str):
    """
    The `console_extra_log` function is a decorator that adds an extra log message to the console after a function is executed.

    Args:
      msg: The `msg` parameter in the `console_extra_log` function is a message that will be printed to the console when the decorated function is called.

    Returns:
      The `decorator_function` is being returned.
    """

    def decorator_function(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(msg)
            return result

        return wrapper

    return decorator_function


def log_date(msg: str):
    """
    The `log_date` function is a decorator that logs a message with the current date before and after calling the decorated function.

    Args:
      msg (str): The `msg` parameter in the `log_date` function is a string that represents the message you want to log along with the date when a decorated function is called.

    Returns:
      The `log_date` function is returning a decorator function that can be used to add logging functionality to other functions.
    """
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{Fore.BLUE + Style.BRIGHT}[{date}] {msg}.{Style.RESET_ALL}")
            return result

        return wrapper

    return decorator_function
