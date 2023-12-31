"""
All main fixtures for automation framework are located here
"""
import pytest

from config.read_config import GetConfig
from utils.start_browser import RunBrowser
from utils import globl, log


@pytest.fixture(scope="class")
def driver(request):
    """
    This fixture reads config file, setup logging and starts appropriate webbrowser.
    :param request: pytest fixture
    :return:
    """

    # Get configuration settings
    config = GetConfig()
    config.read_all_sections()

    # Initiate logging
    log.custom_logger()

    # Start browser for testing
    log.message("Preparing driver.")
    browser_instance = RunBrowser(globl.browser, globl.url)
    request.cls.driver = browser_instance.driver

    yield

    browser_instance.driver.quit()
    log.close_logger()
