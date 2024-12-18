"""
All main fixtures for automation framework are located here
"""
import os
import pytest

from config.read_config import GetConfig
from utils.start_browser import RunBrowser
from utils import globl, log


@pytest.fixture(scope="session", autouse=True)
def get_config():
    """
    This fixture reads config file

    :return:
            Nothing
    """
    # Get configuration settings
    config = GetConfig()
    config.read_all_sections()

    return


@pytest.fixture(scope="session", autouse=True)
def driver(get_config):
    """
    This fixture starts configured web-browser.

    :return:
            Selenium Web-driver
    """
    # Start browser for testing
    browser_instance = RunBrowser(globl.browser, globl.url)

    yield browser_instance.driver

    browser_instance.driver.quit()


@pytest.fixture(scope="module", autouse=True)
def setup_logging():
    """
    This fixture setup logging.

    :return:
            Nothing
    """
    # Initiate logging
    log.custom_logger(globl.logging_level)

    yield

    log.close_logger()


@pytest.fixture(scope="function", autouse=True)
def test_separator():
    """
    This fixture separates test methods in log file and resets test counters
    :return:
            Nothing
    """
    globl.test_method_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split(' ')[0]

    log.message('*******************************************************')
    log.message('**************** TEST SCENARIO START ******************')
    log.message('*******************************************************')

    indentation = (55 - len(globl.test_method_name) - 6) // 2
    log.message(' ' * indentation + 'Test: ' + globl.test_method_name)
    log.message('*******************************************************')

    yield

    log.message('*******************************************************')
    log.message('*************** TEST SCENARIO SUMMARY *****************')
    log.message('*******************************************************')

    log.message(' ' * 4 + 'total_checkpoints: ' + str(globl.test_counters['total_checkpoints']))
    log.message(' ' * 4 + 'total_warnings: ' + str(globl.test_counters['total_warnings']))
    log.message(' ' * 4 + 'total_errors: ' + str(globl.test_counters['total_errors']))
    log.message(' ' * 4 + 'total_exceptions: ' + str(globl.test_counters['total_exceptions']))

    log.message('*******************************************************\n')

    # Reset test counters
    globl.test_counters['total_checkpoints'] = 0
    globl.test_counters['total_warnings'] = 0
    globl.test_counters['total_errors'] = 0
    globl.test_counters['total_exceptions'] = 0

