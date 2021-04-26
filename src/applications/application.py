import os
from typing import Dict

from colorama import Fore  # for colors of the output
from constants import DESCRIPTION_COLOR, QUESTION_COLOR, ERROR_COLOR


class Application:
    """
    Class that describes entities of applications.xml
    """
    def __init__(
            self,
            name: str,
            description: str,
            comment: str,
            url: str,
            paid: bool,
            installation_commands: Dict[str, str],
            deletion_commands: Dict[str, str]
    ) -> None:
        self.name = name
        self.description = description
        self.comment = comment
        self.url = url
        self.paid = paid
        self.installation_commands = installation_commands
        self.deletion_commands = deletion_commands

    def print_informations(self) -> None:
        """
        Print all the informations about the app.
        """
        print(DESCRIPTION_COLOR + "Application name: " + Fore.RESET + self.name)
        print(DESCRIPTION_COLOR + "Description: " + Fore.RESET + self.description)
        print(DESCRIPTION_COLOR + "Comment: " + Fore.RESET + self.comment)
        print(DESCRIPTION_COLOR + "URL: " + Fore.RESET + self.url)
        print(DESCRIPTION_COLOR + "Paid: " + Fore.RESET + str(self.paid))

        # print all the possibles pm inline
        print(Fore.MAGENTA + "Supported package managers: " + Fore.RESET, end="")
        for possible_pm in self.installation_commands.keys():
            print(possible_pm, end=" ")
        print()

    def ask_for_installation(self) -> bool:
        """
        Ask to the user if they want to install the applications
        :return: if the user wants to install the applications
        """
        install_application_choice = input(
            QUESTION_COLOR
            + "Do you want to install " + self.name + "? (y/N): "
            + Fore.RESET
        )
        return install_application_choice in ("y", "Y")

    def install(self, usable_pms: set[str]) -> None:
        """
        Install the applications after asking to the user which PM use
        """
        possibles_pm = list(set(self.installation_commands.keys()) & usable_pms)

        # getting the wanted PM by printing the list of possibles PM and asking which use
        choice = 0
        while not 1 <= choice <= len(possibles_pm):
            print(DESCRIPTION_COLOR, "Possible package managers:")
            for index in range(len(possibles_pm)):
                print(
                    DESCRIPTION_COLOR
                    + str(index + 1) + ": "
                    + Fore.RESET
                    + possibles_pm[index]
                )
            choice = input(
                QUESTION_COLOR
                + "Enter the number of the package manager you want to use (-1 to cancel the installation): "
                + Fore.RESET
            )
            if choice == "-1":
                print(
                    ERROR_COLOR
                    + "Installation canceled"
                    + Fore.RESET
                )
                return
            elif not (choice.isnumeric() and 1 <= int(choice) <= len(possibles_pm)):
                print(
                    ERROR_COLOR
                    + "Error: please enter a number between %d and %d" % (1, len(possibles_pm))
                    + Fore.RESET
                )
                choice = 0
            else:
                choice = int(choice)
        pm = possibles_pm[choice - 1]

        print("Installation with " + pm + ":")
        command = self.installation_commands.get(pm)
        os.system(command)

    def delete(self, used_pm: str) -> None:
        command = self.deletion_commands.get(used_pm)
        os.system(command)
