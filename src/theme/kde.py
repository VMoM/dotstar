import os  # for executing the commands


def install_kde_theme(theme_name: str, theme_folder_path: str) -> None:
    """
    Check that every needed software is here, then start to install the KDE theme
    """
    # Checking that every command is available
    commands_to_check = ["kpackagetool5", "lookandfeeltool"]
    for command in commands_to_check:
        check_command = "type " + command + " > /dev/null 2>&1"
        # The execution will return 0 if present, else an other number. So it's not bool(command)
        command_available = not bool(os.system(check_command))

        if not command_available:
            print("Error: " + command + " is needed but not find. Theme install canceled.")
            return

    installation_command = "kpackagetool5 -i " + theme_folder_path
    installation_failed = bool(os.system(installation_command))

    if installation_failed:
        print("Error: impossible to install the theme.")
        return

    setting_the_theme_command = "lookandfeeltool --apply " + theme_name
    setting_failed = bool(os.system(setting_the_theme_command))

    if setting_failed:
        print("Error: impossible to set the theme.")
    else:
        print("Theme successfully installed.")
        print(
            "Note that with KDE a bug can occur when changing window style:",
            "if you have a white strip on some window (like the setting app),",
            "change the color decoration to a light-one that then re-change it to Sweet-Dark."
        )