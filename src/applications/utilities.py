import os
import json

import ui

import applications.constants as app_constants
from applications.application import Application
from applications.package_manager import PackageManager


def read_application_store(filename: str) -> dict[str, list[Application]]:
    """
    Extracts the applications from the asked file

    :param filename: name of the file where the applications are stored (json)
    :return: a dictionary of applications with the name of each category as a key (Text editors for example) and
             the list of applications in this category as a value
    """
    with open(filename, "r") as applications_file:
        all_application_data = json.load(applications_file)

        # application_store is a dictionary of applications with
        # - the name of each category as a key (Text editors for example)
        # - the list of applications in this category as a value
        application_store: dict[str, list[Application]] = {}

        # filling the application store from the JSON
        for category_name in all_application_data:
            for this_application_data in all_application_data[category_name]:
                # if the category is missing we add it
                if category_name not in application_store.keys():
                    application_store[category_name] = []

                available_pm_for_this_app: dict[PackageManager, str] = {}
                for pm_name in this_application_data["PMs"]:
                    available_pm_for_this_app[
                        app_constants.SUPPORTED_PMS[pm_name]
                    ] = this_application_data["PMs"][pm_name]

                # adding a new Application in the list of the tag
                application_store[category_name].append(
                    Application(
                        this_application_data["name"],
                        this_application_data["description"],
                        this_application_data["comment"],
                        this_application_data["url"],
                        this_application_data["paid"],
                        available_pm_for_this_app
                    )
                )
        return application_store


def get_usable_pms() -> dict[str, PackageManager]:
    """
    Look for supported package managers that are usable on the user's computer

    :return: a dict of usable PackageManager, with their dotstar name as key
    """
    usable_pms = dict()
    for supported_pm_name in app_constants.SUPPORTED_PMS.keys():
        command_to_check_existence = \
            "type " + app_constants.SUPPORTED_PMS[supported_pm_name].system_name \
            + " > /dev/null 2>&1"
        if os.system(command_to_check_existence) == 0:
            usable_pms[supported_pm_name] = app_constants.SUPPORTED_PMS[supported_pm_name]

    return usable_pms


def create_installation_dict(usable_pm: dict[str, PackageManager]) -> dict[PackageManager, list[str]]:
    """
    :return: a dict with each usable PackageManager as key and an empty list as value
    """
    installation_dict: dict[PackageManager, list[str]] = {}
    for pm in usable_pm.values():
        installation_dict[pm] = []

    return installation_dict


def install_apps(installation_dict: dict[PackageManager, list[str]]) -> None:
    """
    Installs all the given apps with their respective package manager

    :param installation_dict: a dict with usable PackageManager as key and a list of application names as value
    """
    for pm in installation_dict.keys():
        if pm.multiple_apps_query_support and len(installation_dict[pm]) > 0:
            all_apps_to_install = " ".join(installation_dict[pm])
            command = pm.command_shape % all_apps_to_install
            ui.print_information("The following installation command will be executed: " + command)
            ui.exec_system(command)
        else:
            for app_name in installation_dict[pm]:
                command = pm.command_shape % app_name
                ui.print_information("The following installation command will be executed: " + command)
                ui.exec_system(command)
