import time

from pages.main.abc_page import ABCPage
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import log


class BasePage(ABCPage):

    def __init__(self, driver: webdriver.Firefox, url: str):
        self.driver = driver
        self.url = url
        self.actions = ActionChains(driver)

    def enter_text_in_search_field(self, text: str):
        """
        Enters text in search field

        :param text: product which need to be found
        :return:
                nothing
        """
        elem_search_field = self.driver.find_element(By.XPATH, "//input[@id='search']")

        log.message(f"Enter text '{text}' in search field.")
        self.actions.move_to_element(elem_search_field).click().send_keys(text).perform()

    def click_search(self):
        """
        Click button search in search field

        :return:
                nothing
        """
        elem_search = self.driver.find_element(By.XPATH, "//button[@class='action search']")
        for iteration in range(10):
            if elem_search.is_enabled():
                log.message("Click Search button.")
                self.actions.move_to_element(elem_search).send_keys(Keys.ENTER).perform()
                return
            else:
                log.message(f"Search button is disabled, waiting 0.5 seconds (iteration: {iteration})")
                time.sleep(0.5)

        log.error("Search button is disabled and can't be clicked.")

    def wait_loading_page(self, timeout=60):
        """
        Wait while page is loading

        :param timeout: wait time in seconds
        :return:

        """
        log.message("Method wait_loading_page() should be defined!!!!")

    def sign_in(self):
        log.message("Method sign_in() should be defined!!!!")

    def create_account(self):
        log.message("Method create_account() should be defined!!!!")

    def search_products(self):
        log.message("Method search_products() should be defined!!!!")

    def open_cart(self):
        log.message("Method open_cart() should be defined!!!!")

    def verify_cart_counter(self):
        log.message("Method verify_cart_counter() should be defined!!!!")

    def verify_cart_subtotal(self):
        log.message("Method verify_cart_subtotal() should be defined!!!!")

    def click_proceed_to_checkout(self):
        log.message("Method click_proceed_to_checkout() should be defined!!!!")

    def click_view_and_edit_cart(self):
        log.message("Method click_view_and_edit_cart() should be defined!!!!")

