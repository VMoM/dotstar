from typing import Optional
from colorama import Fore  # for colors of the output

import ui
from applications.package_manager import PackageManager


class Application:
    """
    Class that describes entities of applications.json
    """
    def __init__(
            self,
            name: str,
            description: str,
            comment: str,
            url: str,
            paid: bool,
            pms: dict[PackageManager, str]
    ) -> None:
        self.name = name
        self.description = description
        self.comment = comment
        self.url = url
        self.paid = paid
        self.pms = pms

    def print_informations(self) -> None:
        """
        Print all the informations about the app.
        """
        ui.print_description("Application name: " + self.name)
        ui.print_description("Description: " + self.description)
        ui.print_description("Comment: " + self.comment)
        ui.print_description("URL: " + self.url)
        ui.print_description("Paid: " + ("yes" if self.paid else "no"))

        # print all the possibles pm inline
        supported_pm = ""
        for possible_pm in self.pms.keys():
            supported_pm += possible_pm.system_name + " "
        ui.print_description("Supported package managers: " + str(supported_pm))

    def ask_for_installation(self) -> bool:
        """
        Ask to the user if they want to install the applications
        :return: if the user wants to install the applications
        """
        install_application_choice = ui.ask("Do you want to install " + self.name + "? (y/N): ")
        return install_application_choice in ("y", "Y")

    def ask_pm(self, usable_pms: dict[str, PackageManager]) -> Optional[PackageManager]:
        """
        Ask to the user witch PM use for the installation
        :return: the PM to use, or None if cancel
        """
        possibles_pm = list(set(self.pms.keys()) & set(usable_pms.values()))
        choice = 0

        while not 1 <= choice <= len(possibles_pm):
            ui.print_information("Possible package managers:")
            for index in range(len(possibles_pm)):
                ui.print_description(
                    str(index + 1) + ": " + possibles_pm[index].system_name
                )
            choice = ui.ask(
                "Enter the number of the package manager you want to use (-1 to cancel the installation): "
            )
            if choice == "-1":
                ui.print_error("Installation canceled")
                return None
            elif not (choice.isnumeric() and 1 <= int(choice) <= len(possibles_pm)):
                ui.print_error("Error: please enter a number between %d and %d" % (1, len(possibles_pm)))
                choice = 0
            else:
                choice = int(choice)

        return possibles_pm[choice - 1]
