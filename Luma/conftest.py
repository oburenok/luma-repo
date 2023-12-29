"""
All main fixtures for automation framework are located here
"""
import pytest
import os

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
    browser_instance = RunBrowser(globl.browser, globl.url)

    yield browser_instance.driver

    browser_instance.driver.quit()
    log.close_logger()
