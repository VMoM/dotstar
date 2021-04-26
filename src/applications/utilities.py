import os

from applications.constants import SUPPORTED_PMS


def get_usable_pms() -> set[str]:
    usable_pms = set()
    for supported_pm in SUPPORTED_PMS:
        command_to_check_existing = "type " + supported_pm + " > /dev/null 2>&1"
        if os.system(command_to_check_existing) == 0:
            usable_pms.add(supported_pm)

    return usable_pms
