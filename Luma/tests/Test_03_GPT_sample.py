"""
This is a first test for commercial website Luma.
"""

import pytest
import time

from utils import log


@pytest.mark.usefixtures("driver")
class Test03GPTsample:

    def test_example_1(self):
        self.driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
        log.screenshot("bla-bla-bla")
        log.message("bla-bla-bla")
        log.message("Some comments")

        log.error("Log error to increase error counter.")
        assert True

    def test_example_2(self):
        self.driver.get("https://www.google.com.ua")
        log.warning("It is warning message.")
        time.sleep(1.5)

