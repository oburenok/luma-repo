from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import log


class Mediator(object):

    def __init__(self, driver: webdriver.Firefox, url: str):
        self.driver = driver
        self.url = url

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
        element = WebDriverWait(self.driver, timeout, poll_frequency=1).until(
            EC.visibility_of_element_located(loc))

        return element

