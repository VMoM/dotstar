from os import path


WORKING_DIR = path.dirname(__file__)
RES_DIR = path.join(WORKING_DIR, "..", "res")


def get_res(res_path: str) -> str:
    """
    :param res_path: path to a ressource from the res directory
    :return: absolute path to the ressource
    """
    return path.join(RES_DIR, res_path)
