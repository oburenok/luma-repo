"""
BasePage for all pages.
"""

import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pages.main.abc_page import ABCPage
from pages.main.mediator import Mediator
from utils import log, verify


class BasePage(ABCPage, Mediator):
    """This is the main parent class for all pages.
    It contains main functionality related to all pages."""

    def __init__(self, driver, url):
        Mediator.__init__(self, driver, url)
        self.actions = ActionChains(driver)
        self.category_menu = CategoryMenu(self.driver, self.url)
        self.cart = Cart(self.driver, self.url)

    page_url = "https://magento.softwaretestingboard.com"
    locator = {
        "search": ["elem_type", (By.XPATH, "//input[@id='search']")],
        "search_btn": ["elem_type", (By.XPATH, "//button[@class='action search']")],
        "cart": ["elem_type", (By.XPATH, "//a[@class='action showcart']")],
        "sign_in": ["elem_type", (By.XPATH, "//header//a[contains(text(),'Sign In')]")],
        "create_account": ["elem_type", (By.XPATH, "//header//a[contains(text(),'Create an Account')]")]
        }

    def enter_text_in_search_field(self, text: str):
        """
        Enters text in search field

        :param text: product which need to be found
        :return:
                nothing
        """
        elem_search_field = self.find_element(self.locator["search"][1])

        log.message("Clean up search field.")
        elem_search_field.send_keys(Keys.CONTROL + 'a')
        elem_search_field.send_keys(Keys.DELETE)

        log.message(f"Enter text '{text}' in search field.")
        self.actions.move_to_element(elem_search_field).click().send_keys(text).perform()

    def click_search(self):
        """
        Click button search in search field

        Example:
            self.results_page.click_search()
        """
        search_btn = self.wait_for_element(self.locator["search_btn"][1])
        search_btn.click()

    def load(self):
        """
        Load page.
        Example:
            self.home_page.load()
        """
        self.driver.get(self.page_url)

    def navigate_to_page(self, link):
        """
        Navigate to specified page by link

        :param link: link to the page
        :type link: str

        """
        self.open_page(url=link)

    def sign_in(self):
        """To be defined"""
        log.message("Method sign_in() should be defined!!!!")

    def create_account(self):
        """To be defined"""
        log.message("Method create_account() should be defined!!!!")

    def search_products(self):
        """To be defined"""
        log.message("Method search_products() should be defined!!!!")

    def open_cart(self):
        """To be defined"""
        log.message("Method open_cart() should be defined!!!!")

    def verify_cart_counter(self):
        """To be defined"""
        log.message("Method verify_cart_counter() should be defined!!!!")

    def verify_cart_subtotal(self):
        """To be defined"""
        log.message("Method verify_cart_subtotal() should be defined!!!!")

    def click_proceed_to_checkout(self):
        """To be defined"""
        log.message("Method click_proceed_to_checkout() should be defined!!!!")

    def logout(self):
        """To be defined"""
        log.message("Method logout() should be defined!!!!")


class CategoryMenu:
    """This class used to navigate through the Category Menu."""

    def __init__(self, driver: webdriver.Firefox, url: str):
        self.driver = driver
        self.url = url
        self.actions = ActionChains(driver)
        self.init_fields()

    def init_fields(self):
        """
        Initialize all elements/fields related to Category Menu
        :return:
        """
        self.locators = {
            "watsnew": "//a[@id='ui-id-3']",
            "woman": "//a[@id='ui-id-4']",
            "wtops": "//a[@id='ui-id-9']",
            "wjackets": "//a[@id='ui-id-11']",
            "whoodies&sweatshirts": "//a[@id='ui-id-12']",
            "wtees": "//a[@id='ui-id-13']",
            "wbras&tanks": "//a[@id='ui-id-14']",
            "wbottoms": "//a[@id='ui-id-10']",
            "wpants": "//a[@id='ui-id-15']",
            "wshorts": "//a[@id='ui-id-16']",

            "man": "//a[@id='ui-id-5']",
            "mtops": "//a[@id='ui-id-17']",
            "mjackets": "//a[@id='ui-id-19']",
            "mhoodies&sweatshirts": "//a[@id='ui-id-20']",
            "mtees": "//a[@id='ui-id-21']",
            "tanks": "//a[@id='ui-id-22']",
            "mbottoms": "//a[@id='ui-id-18']",
            "mpants": "//a[@id='ui-id-23']",
            "mshorts": "//a[@id='ui-id-24']",

            "gear": "//a[@id='ui-id-6']",
            "bags": "//a[@id='ui-id-25']",
            "fitnessequipment": "//a[@id='ui-id-26']",
            "Watches": "//a[@id='ui-id-27']",

            "training": "//a[@id='ui-id-7']",
            "sale": "//a[@id='ui-id-8']"
        }

    def navigate_to_category(self, category_path, click=True):
        """
        Navigate to category

        :param category_path: path to needed product category
        :type category_path: str
        :param click: define if menu item should be clicked or not
        :type click: bool

        Example:
                self.home_page.category_menu.navigate_to_category("woman wtops wjackets")
        :return:
        """
        log.message(f"Navigating to category menu '{category_path}'.")
        for item in category_path.split(" "):
            menu_item = self.driver.find_element(By.XPATH, self.locators[item])

            for iteration in range(10):
                if menu_item.is_displayed():
                    self.actions.move_to_element(menu_item).perform()
                    break
                else:
                    time.sleep(0.5)
            else:
                log.warning("Menu item is not displayed or missing.")

            if click is True and item == category_path.split(" ")[-1]:
                menu_item.click()


class Cart(Mediator):
    """This class is used to work with mini cart on all pages of Luma web-site."""

    def __init__(self, driver: webdriver.Firefox, url: str):
        Mediator.__init__(self, driver, url)

    cart_locator = {
        "title_qty": ["elem_type", (By.XPATH, "//span[@class='counter-number']")]
    }

    def verify_title_quantity(self, expected_qty):
        """
        Verify product quantity next to the cart icon

        :param expected_qty: product quantity
        :type expected_qty: int
        """
        aqtual_qty = self.get_element_text(self.cart_locator["title_qty"][1])

        verify.is_equal(str(aqtual_qty), str(expected_qty),
                        f"Product quantity next to the cart icon should be '{expected_qty}'.")
