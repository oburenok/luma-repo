"""
Logging and settings
"""

import logging
import os
import datetime as dt
import pyautogui


from utils import globl


logger_name = "Custom Logger"


def custom_logger(log_level=logging.INFO):
    """
    This function creates and setup custom logger

    :param log_level: log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :type log_level: int
    :return:
            logger
    """
    # Gets the name of the class / method from where this method is called
    # logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    report_path = globl.reports_path + '\\' + globl.test_name + '.log'

    file_handler = logging.FileHandler(report_path, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def screenshot(suffix='', **kwargs):
    """
    This function takes screenshot and saves in the report folder
    :param suffix: suffix added to the file name. Should not have blank spaces.
    :type suffix: str
    :param kwargs:

    :return:
            screenshot_full_path: str - full path to screenshot file
    """
    dt_now = dt.datetime.now()
    time_stamp = dt_now.strftime("%H%M%S%f")
    date_stamp = dt_now.strftime("%Y%m%d")

    if len(suffix) > 0:
        suffix = '_' + str(suffix)

    file_name = date_stamp + '_' + time_stamp + suffix.replace(' ', '') + '.png'
    file_path = globl.reports_path + '\\screenshots\\'

    screenshot_full_path = file_path + file_name

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    try:
        screen_shot = pyautogui.screenshot()
        screen_shot.save(screenshot_full_path)
    except Exception:
        message("An ERROR occurred while trying to take screenshot " + screenshot_full_path)

    message("Screenshot: " + screenshot_full_path)

    return screenshot_full_path


def message(msg):
    """
    This function adding simple massege in the log file with log level INFO
    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(logger_name)
    logger.info(str(msg))


def warning(msg):
    """
    This function adding warning message in the log file with log level WARNING
    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(logger_name)

    screenshot("WARNING")
    logger.warning(str(msg))


def error(msg):
    """
    This function adding error message in the log file with log level ERROR
    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(logger_name)

    screenshot("ERROR")
    logger.error(str(msg))


def critical(msg):
    """
    This function adding critical message in the log file with log level CRITICAL
    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(logger_name)

    screenshot("CRITICAL")
    logger.critical(str(msg))


def close_logger():
    """
    This function close logger

    :return:
            Nothing
    """
    logging.shutdown()

