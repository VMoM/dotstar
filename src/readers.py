from typing import Dict, List
import json

from applications.application import Application


def read_application_store(filename: str) -> Dict[str, List[Application]]:
    """
    Extracts from the file asked the list of applications
    :param filename: name of the file where the applications are stored (json)
    :return: a dictionary of applications with the name of each category as a key and
             the list of applications in this category as a value
    """
    with open(filename, "r") as applications_file:
        applications_data = json.load(applications_file)

        # application_store is a dictionary of applications with
        # - the name of each category as a key
        # - the list of applications in this category as a value
        application_store: Dict[str, List[Application]] = {}

        # filling the application store from the JSON
        for category_name in applications_data:
            for application_data in applications_data[category_name]:
                # if the category is missing we add it
                if category_name not in application_store.keys():
                    application_store[category_name] = []

                # adding a new Application in the list of the tag
                application_store[category_name].append(
                    Application(
                        application_data["name"],
                        application_data["description"],
                        application_data["comment"],
                        application_data["url"],
                        application_data["paid"],
                        application_data["PMs"]
                    )
                )

        return application_store
