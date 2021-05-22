import subprocess  # for executing some commands

import ui


def install_kde_theme(theme_name: str, theme_folder_path: str) -> None:
    """
    Check that every needed software is here, then start to install the KDE theme
    """
    # Checking that every command is available
    commands_to_check = ["kpackagetool5", "lookandfeeltool"]
    for command in commands_to_check:
        check_command = "type " + command + " > /dev/null 2>&1"
        # The execution will return 0 if present, else an other number. So it's not bool(command)
        command_available = not bool(ui.exec_system(check_command))

        if not command_available:
            ui.print_error("Error: " + command + " is needed but not find. Theme install canceled.")
            return

    ui.print_information("Checking if already installed...")
    check_install_result = subprocess.run(['lookandfeeltool', '-l'], stdout=subprocess.PIPE)
    already_installed = theme_name in check_install_result.stdout.decode("utf-8")
    if already_installed:
        ui.print_information(theme_name + " already installed. Updating...")
        update_command = "kpackagetool5 -u " + theme_folder_path
        update_failed = bool(ui.exec_system(update_command))
        if update_failed:
            ui.print_error("Error: impossible to update the theme.")
            return

    else:
        ui.print_information(theme_name + " not installed. Installation...")
        installation_command = "kpackagetool5 -i " + theme_folder_path
        installation_failed = bool(ui.exec_system(installation_command))

        if installation_failed:
            ui.print_error("Error: impossible to install the theme.")
            return

    ui.print_information("Theme successfully installed.")
    ui.print_information("Setting the theme...")

    setting_the_theme_command = "lookandfeeltool --apply " + theme_name
    setting_failed = bool(ui.exec_system(setting_the_theme_command))

    if setting_failed:
        ui.print_error("Error: impossible to set the theme.")
    else:
        ui.print_information("Theme successfully set.")
        ui.print_information(
            "Note that with KDE a bug can occur when changing window style:"
            + "if you have a white strip on some window (like the setting app),"
            + "change the color decoration to a light-one that then re-change it to Sweet-Dark."
        )
