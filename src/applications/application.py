import os
from typing import Dict


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
        Print all the informations about the app
        """
        print("Application name:", self.name)
        print("Description:", self.description)
        print("Comment:", self.comment)
        print("URL:", self.url)
        print("Paid:", self.paid)

        # print all the possibles pm inline
        print("Supported package managers: ", end="")
        for possible_pm in self.installation_commands.keys():
            print(possible_pm, end=" ")
        print()

    def ask_for_installation(self) -> bool:
        """
        Ask to the user if they want to install the applications
        :return: if the user wants to install the applications
        """
        install = input("Do you want to install " + self.name + "? (y/N) ")
        return install in ("y", "Y")

    def install(self) -> None:
        """
        Install the applications after asking to the user which PM use
        """
        possibles_pm = list(self.installation_commands.keys())

        # getting the wanted PM
        choice = 0
        while not 1 <= choice <= len(possibles_pm):
            print("Which package manager do you want to use?")
            for i in range(len(possibles_pm)):
                print("%d : %s" % (i+1, possibles_pm[i]))
            choice = input("Enter the corresponding number (-1 to cancel the installation): ")

            if not (choice.isnumeric() and 1 <= int(choice) <= len(possibles_pm)):
                print("Error: please enter a number between %d and %d" % (1, len(possibles_pm)))
            elif choice == "-1":
                return
        pm = possibles_pm[int(choice) - 1]

        command = self.installation_commands.get(pm)
        os.system(command)

    def delete(self, used_pm: str) -> None:
        command = self.deletion_commands.get(used_pm)
        os.system(command)
