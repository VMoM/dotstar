import os  # for getting the DE
import colorama  # for colors with print() and input()

import applications.utilities as app_utils
import theme.kde as kde
import res
import constants


def main() -> None:

    # Application part
    install_applications_choice = input(
        constants.QUESTION_COLOR
        + "Do you want to install applications? (y/N): "
        + colorama.Fore.RESET
    )
    if install_applications_choice in ("y", "Y"):
        application_store = app_utils.read_application_store(res.get_absolute_res_path("applications.json"))

        usable_pms = app_utils.get_usable_pms()
        installation_dict = app_utils.create_installation_dict(usable_pms)

        for category_name in application_store:
            see_category_choice = input(
                constants.QUESTION_COLOR
                + "Do you want to see available applications from the <" + category_name + "> category? (y/N): "
                + colorama.Fore.RESET
            )
            if see_category_choice in ("y", "Y"):
                for application in application_store[category_name]:
                    print(constants.DELIMITER_COLOR + constants.DELIMITER + colorama.Fore.RESET)
                    application.print_informations()
                    install_it = application.ask_for_installation()
                    if install_it:
                        pm = application.ask_pm(usable_pms)
                        if pm is not None:
                            installation_dict[pm].append(application.pms[pm])

        print(constants.DELIMITER_COLOR + constants.DELIMITER + colorama.Fore.RESET)
        print("Installation on the selected apps...")
        app_utils.install_apps(installation_dict)
        print("End of the installation part.")

    # Apparence part
    user_de = os.environ["DESKTOP_SESSION"]
    if user_de in constants.SUPPORTED_DE and input(
        constants.QUESTION_COLOR
        + "Your desktop environment is compatible with the customization. Do you want to customize it? (y/N): "
        + colorama.Fore.RESET
    ) in ("Y", "y"):
        print(
            "My custom theme \"Sweet-Layan-mashup\", a mashup of my two favorites KDE themes ",
            "(Sweet by EliverLara and Layan by Vince Liuice, plus Papirus icon theme) will be install.",
            "You can return to your previous theme by going to apparence/ in the KDE setting app."
        )
        kde.install_kde_theme("Sweet-Layan-mashup", res.get_absolute_res_path("theme/KDE/Sweet-Layan-mashup"))


if __name__ == "__main__":
    main()
