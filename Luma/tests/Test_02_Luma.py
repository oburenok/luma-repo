"""
This is a first test for commercial website Luma.
"""

import pytest
import time

from utils import log


@pytest.mark.usefixtures("driver")
class Test02Luma:

    def test_example_1(self):
        self.driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
        log.message("bla-bla-bla")
        log.message("Some comments")
        log.message("bla-bla-bla")
        log.message("Some comments")

        log.screenshot("bla-bla-bla")

        log.message("bla-bla-bla")
        log.message("Some comments")
        log.message("bla-bla-bla")
        log.message("Some comments")

        log.error("Log error to increase error counter.")

        assert True

    def test_navigation_to_google(self):
        self.driver.get("https://www.google.com.ua")
        log.message("bla-bla-bla")
        log.message("Some comments")
        log.message("bla-bla-bla")
        log.message("Some comments")

        log.warning("It is warning message.")
        log.warning("It is warning message.")

        log.message("Add more comments")
        log.message("to simulate testing process.")

        log.critical("Log critical to increase critical counter.")
        time.sleep(1.5)

