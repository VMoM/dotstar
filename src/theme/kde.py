import subprocess  # for executing some commands
import os
import json

import ui

# some user vars
USER_HOME_PATH = os.popen("echo $HOME").read().strip() + "/"
CONFIG_PATH = USER_HOME_PATH + ".config/"
LOCAL_PATH = USER_HOME_PATH + ".local/"


def read_json_dependencies(json_path: str) -> dict[str]:
    with open(json_path, "r") as json_file:
        return json.load(json_file)

def install_kde_theme(theme_name: str, theme_folder_path: str) -> None:
    """
    Check that every needed software is here, then start to install the KDE theme
    """

    # Checking that every command is available
    commands_to_check = ["kpackagetool5", "lookandfeeltool", "wget", "tar"]
    for command in commands_to_check:
        check_command = "type " + command + " > /dev/null 2>&1"
        # The execution will return 0 if present, else an other number. So it's not bool(command)
        command_available = not bool(ui.exec_system(check_command))

        if not command_available:
            ui.print_error("Error: " + command + " is needed but not find. Theme install canceled.")
            return

    # looking if the theme is already installed, and deleting it if yes
    check_install_result = subprocess.run(['lookandfeeltool', '-l'], stdout=subprocess.PIPE)
    already_installed = theme_name in check_install_result.stdout.decode("utf-8")
    if already_installed:
        ui.print_information(theme_name + " already installed. Deleting...")
        delete_command = "kpackagetool5 -r " + theme_folder_path
        delete_failed = bool(ui.exec_system(delete_command))
        if delete_failed:
            ui.print_error("Error: impossible to delete the theme.")
            return

    # INSTALLATION OF THE DEPENDENCIES
    theme_dependencies = read_json_dependencies(theme_folder_path + "/dependencies.json")
    dependency_names = [
        "colorscheme",
        "plasma_theme",
        "aurorae",
        "icons",
        "wallpaper",
        "sddmtheme",
        "xcursor"
    ]
    # TODO find where other dependencies are
    dependency_paths = [
        LOCAL_PATH + "share/icons"
    ]
    for i in range(len(dependency_names)):
        ui.print_information("Installation of the %s" % dependency_names[i])
        component_installation_command = (
                "sh "
                + os.path.dirname(__file__) + "/install_theme_component.sh"
                + " " + theme_dependencies[dependency_names[i]]["download_link"]
                + " " + theme_dependencies[dependency_names[i]]["archive_name"]
                + " " + dependency_paths[i]
        )
        icon_installation_failed = bool(ui.exec_system(component_installation_command))
        if icon_installation_failed:
            ui.print_error("Error: impossible to install %s." % dependency_names[i])
            return

    ui.print_information("Installation of %s (the global theme)..." % theme_name)
    installation_command = "kpackagetool5 -i " + theme_folder_path
    installation_failed = bool(ui.exec_system(installation_command))

    if installation_failed:
        ui.print_error("Error: impossible to install the global theme.")
        return

    ui.print_information("Global theme successfully installed.")
    ui.print_information("Setting the theme...")

    setting_the_theme_command = "lookandfeeltool --apply " + theme_name
    setting_failed = bool(ui.exec_system(setting_the_theme_command))

    if setting_failed:
        ui.print_error("Error: impossible to set the global theme.")
    else:
        ui.print_information("Global theme successfully set.")
        ui.print_information(
            "Note that with KDE a bug can occur when changing window style:"
            + "if you have a white strip on some window (like the setting app),"
            + "change the color decoration to a light-one that then re-change it to Sweet-Dark."
        )
