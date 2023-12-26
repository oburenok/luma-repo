"""
All main fixtures for automation framework are located here
"""
import pytest

from config.read_config import GetConfig
from utils.start_browser import RunBrowser
from utils import globl, log


def pytest_configure():
    pytest.browser = "Some browser"
    pytest.url = "https://google.com.ua"


@pytest.fixture(scope="module")
def driver():

    # Get configuration settings
    config = GetConfig()
    config.read_all_sections()

    # Initiate logging
    log.custom_logger()

    # Start browser for testing
    log.message("Preparing driver.")
    browse_driver = RunBrowser(globl.browser, globl.url)
    yield browse_driver.driver

    browse_driver.driver.quit()
