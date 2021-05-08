import os

from applications.constants import SUPPORTED_PMS


def get_usable_pms() -> set[str]:
    usable_pms = set()
    for supported_pm_name in SUPPORTED_PMS:
        command_to_check_existing = "type " + SUPPORTED_PMS[supported_pm_name] + " > /dev/null 2>&1"
        if os.system(command_to_check_existing) == 0:
            usable_pms.add(supported_pm_name)

    return usable_pms


def create_installation_dict(usable_pm: set[str]) -> dict[str, list[str]]:
    installation_dict: dict[str, list[str]] = {}
    for pm in usable_pm:
        installation_dict[pm] = []

    return installation_dict


def install_apps(installation_dict: dict[str, list[str]]):
    for pm in installation_dict:
        if len(installation_dict[pm]) != 0:
            command = "sudo "
            if pm == "snap classic" or pm == "snap sandbox":
                command += "snap install "
            elif pm == "pacman":
                command += "pacman -Sy "
            else:
                raise ValueError("Error: unknown package manager : " + pm)

            for package_name in installation_dict[pm]:
                command += package_name + " "

            if pm == "snap classic":
                command += "--classic"

            print("The following installation command will be executed: " + command)
            os.system(command)

