from readers import read_application_store
from res import get_res


def main() -> None:

    # Application part
    print("Do you want to install applications?")
    install_applications = input("Your answer (y/N): ") in ("y", "Y")
    if install_applications:
        application_store = read_application_store(get_res("applications.xml"))

        for category_name in application_store:
            for application in application_store[category_name]:
                print("##################################################")
                application.print_informations()
                install_it = application.ask_for_installation()
                if install_it:
                    application.install()

    # Apparence part
    # (WIP)


if __name__ == "__main__":
    main()
