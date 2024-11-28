"""
Module contains all functions for saving/excluding testing data in/from file
"""
import pickle

from utils import globl, log


def store(data, **kwargs):
    """
    Saves testing data

    :param data: data to be saved.
    :type data: obj
    """
    file_name = kwargs.get("file_name", f"{globl.test_name}.pickle")

    log.message(f"Saving testing data to file '{file_name}'.")
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(data, file)
            file.close()
    except Exception as exc:
        log.exception(str(exc))


def exclude(**kwargs):
    """
    Exclude testing data from file

    :return: object from file
    """
    file_name = kwargs.get("file_name", f"{globl.test_name}.pickle")

    log.message(f"Excluding testing data from file '{file_name}'.")
    try:
        with open(file_name, 'rb') as file:
            file_object = pickle.load(file)
    except Exception as exc:
        log.exception(str(exc))

    return file_object
