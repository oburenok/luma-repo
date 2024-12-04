import copy

from pages.main.base import BasePage
from pages.main.mediator import Mediator
from pages.main.abc_product import ABCProduct
from selenium.webdriver.common.by import By
from utils import verify


class CartPage(BasePage):
    page_url = "https://magento.softwaretestingboard.com/checkout/cart/"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)
        self.product = CartProduct(self.driver, self.url)

    cart_locator = {"proceed_to_checkout": ["elem_type", (By.XPATH, "//button[@data-role='proceed-to-checkout']")]}

    def click_proceed_to_checkout(self):
        """
        Click Proceed to Checkout button

        """
        elem_button = self.find_element(self.cart_locator["proceed_to_checkout"][1])
        self.click_element(elem_button)


class CartProduct(ABCProduct, Mediator):

    def __init__(self, driver, url: str):
        Mediator.__init__(self, driver, url)

    __prod_locator = {
        "products_list": ["elem_type", (By.XPATH, "//tbody[@class='cart item']")],
        "name": ["elem_type", (By.XPATH, "//tbody[@class='cart item']//a[contains(text(),'PRODUCT_NAME')]")],
        "size": ["elem_type", (By.XPATH,
                               "//tbody[@class='cart item']//a[contains(text(),"
                               "'PRODUCT_NAME')]//parent::strong//following-sibling::dl/dd[1]")],
        "color": ["elem_type", (By.XPATH,
                                "//tbody[@class='cart item']//a[contains(text(),"
                                "'PRODUCT_NAME')]//parent::strong//following-sibling::dl/dd[2]")],
        "price": ["elem_type",
                  (By.XPATH, "(//tbody[@class='cart item']//a[contains(text(),"
                             "'PRODUCT_NAME')]/parent::strong/parent::div/parent::td/following-sibling::td//span["
                             "@class='price'])[1]")],
        "subtotal": ["elem_type",
                     (By.XPATH,
                      "(//tbody[@class='cart item']//a[contains(text(),"
                      "'PRODUCT_NAME')]/parent::strong/parent::div/parent::td/following-sibling::td//span["
                      "@class='price'])[2]")],
        "qty": ["elem_type", (By.XPATH, "//tbody[@class='cart item']//a[contains(text(),"
                                        "'PRODUCT_NAME')]/parent::strong/parent::div/parent::td/following-sibling::td"
                                        "//input[@class='input-text qty']")],
    }

    def get_price(self):
        """
        CAN'T BE IMPLEMENTED ON CART PAGE

        :return: str, price
        """
        # elem_price = self.get_element_text(self.__prod_locator["price"][1])
        #
        # # removing symbol $
        # elem_price = elem_price[1:]
        #
        # return elem_price
        pass

    def verify_price(self, prod_name, expected_price: str):
        """
        Verifies price of the product

        :param prod_name: product name
        :type prod_name: str
        :param expected_price: product price, without $ symbol
        :type expected_price: str
        """
        locator = (
            self.__prod_locator["price"][1][0],
            self.__prod_locator["price"][1][1].replace('PRODUCT_NAME', prod_name))
        actual_price = self.get_element_text(locator)

        # removing symbol $
        actual_price = actual_price[1:]

        verify.is_equal(actual_price, expected_price, f"Product price should be '{expected_price}'.")

    def verify_subtotal(self, prod_name, expected_subtotal: str):
        """
        Verifies price of the product

        :param prod_name: product name
        :type prod_name: str
        :param expected_subtotal: product subtotal, without $ symbol
        :type expected_subtotal: str
        """
        locator = (
            self.__prod_locator["subtotal"][1][0],
            self.__prod_locator["subtotal"][1][1].replace('PRODUCT_NAME', prod_name))
        actual_subtotal = self.get_element_text(locator)

        # removing symbol $
        actual_subtotal = actual_subtotal[1:]

        verify.is_equal(actual_subtotal, expected_subtotal, f"Product price should be '{expected_subtotal}'.")

    def get_qty(self):
        """
        CAN'T BE IMPLEMENTED ON CART PAGE

        :return: int, quantity
        """
        # elem_qty = self.find_element(self.__prod_locator["qty"][1])
        #
        # elem_qty = int(elem_qty.get_attribute("value"))
        #
        # return elem_qty
        pass

    def verify_qty(self, prod_name, expected_qty):
        """
        Verifies quantity of the product

        :param prod_name: product name
        :type prod_name: str
        :param expected_qty: product quantity
        :type expected_qty: str

        """
        locator = (
            self.__prod_locator["qty"][1][0],
            self.__prod_locator["qty"][1][1].replace('PRODUCT_NAME', prod_name))

        elem_qty = self.find_element(locator)
        actual_qty = elem_qty.get_attribute("value")

        verify.is_equal(str(actual_qty), str(expected_qty), f"Product quantitye should be '{expected_qty}'.")

    def enter_qty(self, prod_name, qty):
        """
        Enter quantity

        :param prod_name: product name
        :type prod_name: str
        :param qty: product quantity
        :type qty: int
        :return:
        """
        locator = (
            self.__prod_locator["qty"][1][0],
            self.__prod_locator["qty"][1][1].replace('PRODUCT_NAME', prod_name))

        self.enter_value_in_field(locator, qty)

    def get_name(self):
        """
        CAN'T BE IMPLEMENTED ON CART PAGE

        :return: str
        """
        # elem_name = self.get_element_text(self.__prod_locator["name"][1])
        #
        # return elem_name
        pass

    def verify_name(self, prod_name):
        """
        Verifies product name, by checking if product is visible

        :param prod_name: product name
        :type prod_name: str
        """
        locator = (
            self.__prod_locator["name"][1][0],
            self.__prod_locator["name"][1][1].replace('PRODUCT_NAME', prod_name))

        elem_name = self.wait_for_element(locator)

        verify.is_not_equal(elem_name, None, "If element Name is present, it shouldn't be None.")

    def verify_size(self, prod_name, expected_size):
        """
        Verifies product size

        :param prod_name: product name
        :type prod_name: str
        :param expected_size: expected product size
        :type expected_size: str
        """
        locator = (
            self.__prod_locator["size"][1][0],
            self.__prod_locator["size"][1][1].replace('PRODUCT_NAME', prod_name))

        actual_size = self.get_element_text(locator)

        verify.is_equal(actual_size, expected_size, f"Product size should be '{expected_size}'.")

    def verify_color(self, prod_name, expected_color):
        """
        Verifies product color

        :param prod_name: product name
        :type prod_name: str
        :param expected_color: expected product color
        :type expected_color: str
        """
        locator = (
            self.__prod_locator["color"][1][0],
            self.__prod_locator["color"][1][1].replace('PRODUCT_NAME', prod_name))

        actual_color = self.get_element_text(locator)

        verify.is_equal(actual_color, expected_color.capitalize(), f"Product color should be '{expected_color}'.")

    def add_to_cart(self):
        """
        METHOD SHOULD BE REWORKED FOR 'MORE CHOICES' PRODUCTS

        :return: int, quantity
        """
        # button_add = self.find_element(self.__prod_locator["add_to_cart"][1])
        #
        # button_add.click()
        #
        # # Waiting while product is adding to the cart
        # self.wait_for_element(self.__prod_locator["add_to_cart"][1])
        pass

    def select_color(self, color):
        """
        CAN'T BE IMPLEMENTED ON CART PAGE

        :param color: product color
        :type color: str

        Example:
                product.select_color("Orange")
                product.select_color("orange")
        """
        # color = color.capitalize()
        # color_locator = (
        #     self.__prod_locator["color"][1][0],
        #     self.__prod_locator["color"][1][1].replace('COLOR', color))
        #
        # color_elem = self.wait_for_element(color_locator)
        # color_elem.click()
        #
        # return self
        pass

    def select_size(self, size):
        """
        CAN'T BE IMPLEMENTED ON CART PAGE

        :param size: product color
        :type size: str

        Example:
                product.select_size('M')
                product.select_size('xl')
        """
        # size = size.upper()
        #
        # size_locator = (
        #     self.__prod_locator["size"][1][0],
        #     self.__prod_locator["size"][1][1].replace('SIZE', size))
        #
        # color_elem = self.wait_for_element(size_locator)
        # color_elem.click()
        #
        # return self
        pass


class ProductParam:

    def __init__(self, name, size, color, price, qty, subtotal):
        self.name = name
        self.size = size
        self.color = color
        self.price = price
        self.qty = qty
        self.subtotal = subtotal

    def clone(self):
        return copy.deepcopy(self)
