from colorama import Fore
from typing import Any, Callable

import os  # for exec_system

# colors
QUESTION_COLOR = Fore.GREEN
DELIMITER_COLOR = Fore.BLUE
DESCRIPTION_COLOR = Fore.MAGENTA
ERROR_COLOR = Fore.RED
INFORMATION_COLOR = Fore.YELLOW
SYSTEM_COLOR = Fore.CYAN
RESET_COLOR = Fore.RESET

DELIMITER = "##################################################"


def exec_colored(fore: int, func: Callable[[Any], Any], param: Any) -> Any:
    """
    Executes the function with an colored output

    :param fore: color of the output
    :param func: function to execute
    :param param: parameter to give to func
    :return: the result of func
    """
    print(fore, end="")
    result = func(param)
    print(RESET_COLOR, end="")
    return result


def ask(question: str) -> str:
    """
    Asks the question to the user with a colored font

    :param question: text to show before the input
    :return: what the user enters
    """
    return exec_colored(QUESTION_COLOR, input, question + RESET_COLOR)


def print_delimiter() -> None:
    """
    Prints the delimiter with a colored font
    """
    exec_colored(DELIMITER_COLOR, print, DELIMITER)


def print_description(description: str) -> None:
    """
    Prints the description with a colored font
    """
    exec_colored(DESCRIPTION_COLOR, print, description)


def print_error(error_message: str) -> None:
    """
    Prints the error with a colored font
    """
    exec_colored(ERROR_COLOR, print, error_message)


def print_information(information: str) -> None:
    """
    Prints the information with a colored font
    """
    exec_colored(INFORMATION_COLOR, print, information)


def exec_system(command: str) -> int:
    """
    Executes the given system command

    :return: the return code
    """
    # we have to print SYSTEM_COLOR because since in exec_colored the color is put at the beginning of the first line
    # but the all the actual line is deleted with os.system, SYSTEM_COLOR will be ignored else.
    print(SYSTEM_COLOR)
    return exec_colored(SYSTEM_COLOR, os.system, command)
