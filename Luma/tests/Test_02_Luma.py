"""
This is a first test for commercial website Luma.
"""

import pytest
import time

from utils import globl, log


@pytest.mark.usefixtures("driver")
class Test02Luma:
    globl.test_name = 'Test_02_Luma'

    def test_example_1(self, driver):
        driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
        log.screenshot("bla-bla-bla")
        assert True

    def test_example_2(self, driver):
        driver.get("https://www.google.com.ua")
        log.warning("It is warning message.")
        time.sleep(1.5)

