from pages.main.base import BasePage
from pages.main.mediator import Mediator
from pages.main.abc_product import ABCProduct
from selenium.webdriver.common.by import By
from utils import log, verify


class ProductPage(BasePage):

    page_url = "https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)
        self.product = Product(self.driver, self.url)


class Product(ABCProduct, Mediator):

    def __init__(self, driver, url: str):
        Mediator.__init__(self, driver, url)

    __prod_locator = {
        "name": ["elem_type", (By.CSS_SELECTOR, ".page-title")],
        "price": ["elem_type", (By.XPATH, "//div[@class='product-info-price']//span[@class='price']")],
        "qty": ["elem_type", (By.ID, "qty")],
        "color": ["elem_type", (By.XPATH, "//div[@class='product-info-main']//div[@option-label='COLOR']")],
        "size": ["elem_type", (By.XPATH, "//div[@class='product-info-main']//div[@option-label='SIZE']")],
        "add_to_cart": ["elem_type", (By.ID, "product-addtocart-button")],
        "spinning_cyrcle": ["elem_type", (By.CSS_SELECTOR, "[class*='_block-content-loading']")],
    }

    def get_price(self):
        """
        Gets price of the product

        :return: str, price
        """
        elem_price = self.get_element_text(self.__prod_locator["price"][1])

        # removing symbol $
        elem_price = elem_price[1:]

        return elem_price

    def verify_price(self, expected_price: str):
        """
        Verifies price of the product

        :param expected_price: product price, without $ symbol
        :type expected_price: str
        :return:
        """
        actual_price = self.get_price()

        verify.is_equal(actual_price, expected_price, f"Product price should be '{expected_price}'.")

    def get_qty(self):
        """
        Gets quantity of the product

        :return: int, quantity
        """
        elem_qty = self.find_element(self.__prod_locator["qty"][1])

        elem_qty = int(elem_qty.get_attribute("value"))

        return elem_qty

    def verify_qty(self, expected_qty):
        """
        Verifies quantity of the product

        :param expected_qty: product quantity
        :type expected_qty: int

        """
        actual_qty = self.get_qty()

        verify.is_equal(str(actual_qty), str(expected_qty), f"Product quantitye should be '{expected_qty}'.")

    def get_name(self):
        """
        Gets product name

        :return: str
        """
        elem_name = self.get_element_text(self.__prod_locator["name"][1])

        return elem_name

    def verify_name(self, expected_name):
        """
        Verifies product name

        :param expected_name: product name
        :type expected_name: str
        :return:
        """
        actual_name = self.get_name()

        verify.is_equal(actual_name, expected_name, f"Product name should be '{expected_name}'.")

    def add_to_cart(self):
        """
        Gets quantity of the product

        :return: int, quantity
        """
        button_add = self.find_element(self.__prod_locator["add_to_cart"][1])

        button_add.click()

        # Waiting while product is adding to the cart
        self.wait_for_element_disappear(self.__prod_locator["spinning_cyrcle"][1])

    def select_color(self, color):
        """
        Select color of product

        :param color: product color
        :type color: str

        Example:
                product.select_color("Orange")
                product.select_color("orange")
        """
        color = color.capitalize()
        color_locator = (
            self.__prod_locator["color"][1][0],
            self.__prod_locator["color"][1][1].replace('COLOR', color))

        color_elem = self.wait_for_element(color_locator)
        color_elem.click()

        return self

    def select_size(self, size):
        """
        Select size of product

        :param size: product color
        :type size: str

        Example:
                product.select_size('M')
                product.select_size('xl')
        """
        size = size.upper()

        size_locator = (
            self.__prod_locator["size"][1][0],
            self.__prod_locator["size"][1][1].replace('SIZE', size))

        size_elem = self.wait_for_element(size_locator)
        size_elem.click()

        return self

    def enter_qty(self, qty):
        """
        Enter quantity

        :param qty: product quantity
        :type qty: int
        :return:
        """
        self.enter_value_in_field(self.__prod_locator["qty"][1], qty)

