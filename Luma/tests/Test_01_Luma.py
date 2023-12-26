"""
This is a first test for commercial website Luma.
"""

import time
from selenium.webdriver.common.by import By
from utils import globl, log


def test_01(driver):
    time.sleep(1)

    # driver.get("https://magento.softwaretestingboard.com/what-is-new.html")
    #
    # elem = driver.find_element(By.XPATH, "(//li[@class='item']/a[text()='Jackets'])[2]")
    # elem.click()
    #
    # time.sleep(1)
    # log.message("My first log!!!")
    # log.message("Test name is: " + str(globl.test_name))
    #
    # log.screenshot()
    # log.screenshot("bla-bla-bla")
    #
    # log.warning("It is warning message.")
    # log.error("It is error message.")
    log.critical("It is critical message.")
    # log.message(globl.project_name)
    # log.message(globl.project_path)
    log.message(globl.reports_path)

    assert True
