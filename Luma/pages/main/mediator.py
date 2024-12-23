"""
This is the mediator, it contains all methods which call Selenium WebDriver.
"""
import traceback

from selenium import webdriver
from selenium.common import exceptions as exc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import log


class Mediator:
    """This class is the mediator between Page Objects and Selenium WebDriver,
    all operation with driver should be done here."""

    def __init__(self, driver: webdriver.Firefox, url: str):
        self.driver = driver
        self.url = url
        self.actions = ActionChains(driver)

    def find_element(self, loc):
        """
        Find element on the page
        :param loc: locator for element, should look like (By.XPATH, "//input[@id='search']")
        :type loc: tuple

        :return: webelement

        Example:
                self.find_element(self.locator["search_btn"][1])
        """
        return self.driver.find_element(loc[0], loc[1])

    def find_elements(self, loc):
        """
        Find elements on the page
        :param loc: locator for elements, should look like (By.XPATH,
                    "//ol[@class='products list items product-items']/li[@class='item product product-item']")
        :type loc: tuple

        :return: webelement

        Example:
                self.find_elements(self.locator["products_list"][1])
        """
        return self.driver.find_elements(loc[0], loc[1])

    def get_element_text(self, loc):
        """
        Find element text
        :param loc: locator for element, should look like (By.XPATH, "//input[@id='price']")
        :type loc: tuple

        :return: str

        Example:
                self.find_element(self.locator["search_btn"][1])
        """
        return self.find_element(loc).text

    def wait_for_element(self, loc, timeout=60):
        """
        Wait for element

        :param timeout: time to wait in second, before return error
        :param timeout: int
        :param loc: locator for element, should look like (By.XPATH, "//input[@id='price']")
        :type loc: tuple

        :return: webelement

        Example:
            self.wait_for_element(self.locator["search_btn"][1])
        """
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=1).until(
                    EC.visibility_of_element_located(loc))

        except:
            exception_info = traceback.format_exc()
            log.exception(f"An exception occurred while waiting for element!!! \n {exception_info}")

        return element

    def wait_for_ads(self, loc, timeout=60):
        """
        Wait for element

        :param timeout: time to wait in second, before return error
        :param timeout: int
        :param loc: locator for element, should look like (By.XPATH, "//div[@class='grippy-host']//parent::ins")
        :type loc: tuple

        :return: webelement, or False - if element is not found (displayed).

        Example:
            self.wait_for_ads(self.locator["ads"][1], timeout=10)
        """
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=1).until(
                    EC.visibility_of_element_located(loc))

        except exc.TimeoutException:
            log.message("Ads waiting timeout has expired!!!")
            return False

        return element

    def wait_for_element_disappear(self, loc, timeout=60):
        """
        Wait while element disappear

        :param timeout: time to wait in second, before return error
        :param timeout: int
        :param loc: locator for element, should look like (By.CSS_SELECTOR, "[class*='_block-content-loading']")
        :type loc: tuple

        :return: True - if element disappeared
                 False - if element didn't disappear

        Example:

        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=1).until(
                EC.invisibility_of_element(loc))

        except:
            exception_info = traceback.format_exc()
            log.exception(f"An exception occurred while waiting for disappearing element!!! \n {exception_info}")
            return False

        return True

    def open_page(self, url):
        """
        Navigate to specified page by link

        :param url: url of the page
        :type url: str

        Example:
                open_page(url="https://magento.softwaretestingboard.com/antonia-racer-tank.html")
        """
        self.driver.get(url)

    def enter_value_in_field(self, loc, value):
        """
        Enter data in field

        :param loc: locator for element, should look like (By.XPATH, "//input[@id='price']")
        :type loc: tuple
        :param value: text or numeric value
        :type value: str, int

        Example:

        """
        elem_field = self.wait_for_element(loc)

        elem_field.send_keys(Keys.CONTROL + 'a')
        elem_field.send_keys(Keys.DELETE)

        self.actions.move_to_element(elem_field).click().send_keys(value).perform()

    def click_element(self, element):
        """
        Click to element
        :param element: web-element, found by webdriver
        :type element: web-element
        """
        element.click()

    def move_to_element(self, element):
        """
        Find element and move to it
        :param element: web_element, found by webdriver
        :type element: obj element

        Example:
                elem = self.driver.find_elements(By.XPATH, "//input[@id='price']")
                move_to_element(element)
        """
        self.actions.move_to_element(element).perform()

    def scroll_down(self, element):
        """
        Scroll down

        :param element: web_element, found by webdriver
        :type element: obj element
        """
        element.send_keys(Keys.PAGE_DOWN)
