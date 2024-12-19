"""
This is a first test for commercial website Luma.
"""

import pytest

from utils import log

pytestmark = [pytest.mark.run_every_night]


def test_example_1(driver):
    driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
    log.screenshot("bla-bla-bla")
    log.message("bla-bla-bla")
    log.message("Some comments")
    log.debug_message("This debug message.")

    log.error("Log error to increase error counter.")
    assert True


def test_example_2(driver):
    log.debug_message("Debugging test.")
    driver.get("https://www.google.com.ua")
    log.warning("It is warning message.")

