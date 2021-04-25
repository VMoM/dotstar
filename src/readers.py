from typing import Dict, List
import xml.etree.ElementTree as ElementTree

from applications.application import Application


def read_application_store(filename: str) -> Dict[str, List[Application]]:
    """
    Extracts from the file asked the list of applications
    :param filename: name of the file where the applications are stored
    :return: a dictionary of applications with the name of each category as a key and
             the list of applications in this category as a value
    """
    # getting the parent tag
    tree = ElementTree.parse(filename)
    applications_xml = tree.getroot()

    # application_store is a dictionary of applications with
    # - the name of each category as a key
    # - the list of applications in this category as a value
    application_store: Dict[str, List[Application]] = {}

    # filling the application store from the XML
    for application_xml in applications_xml:
        # if the category is missing we add it
        if application_xml.tag not in application_store.keys():
            application_store[application_xml.tag] = []

        # getting installation & deletion commands
        installation_commands = {}
        deletion_commands = {}
        for pm in application_xml:
            installation_commands[pm.tag] = pm.attrib["install"]
            deletion_commands[pm.tag] = pm.attrib["delete"]

        # adding a new Application in the list of the tag
        application_store[application_xml.tag].append(
            Application(
                application_xml.attrib["name"],
                application_xml.attrib["description"],
                application_xml.attrib["comment"],
                application_xml.attrib["url"],
                application_xml.attrib["paid"] == "true",
                installation_commands,
                deletion_commands
            )
        )

    return application_store
