import os  # for getting the DE
from colorama import Fore  # for colors of the output

from readers import read_application_store
from applications.utilities import get_usable_pms
from res import get_absolute_res_path
from constants import QUESTION_COLOR, HASH_COLOR, SUPPORTED_DE


def main() -> None:

    # Application part
    install_applications_choice = input(
        QUESTION_COLOR
        + "Do you want to install applications? (y/N): "
        + Fore.RESET
    )
    if install_applications_choice in ("y", "Y"):
        application_store = read_application_store(get_absolute_res_path("applications.xml"))

        usable_pms = get_usable_pms()
        for category_name in application_store:
            for application in application_store[category_name]:
                print(HASH_COLOR + "##################################################" + Fore.RESET)
                application.print_informations()
                install_it = application.ask_for_installation()
                if install_it:
                    application.install(usable_pms)

        print(HASH_COLOR + "##################################################" + Fore.RESET)
        print("End of the installation part.")

    # Apparence part
    user_de = os.environ["DESKTOP_SESSION"]
    if user_de in SUPPORTED_DE and input(
        QUESTION_COLOR
        + "Your desktop environment is compatible with the customization. Do you want to customize it? (y/N): "
        + Fore.RESET
    ) in ("Y", "y"):
        print("WIP")


if __name__ == "__main__":
    main()
