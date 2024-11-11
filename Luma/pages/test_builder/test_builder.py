
from pages.login_page.login_page import LoginPage
from pages.home_page.home_page import HomePage
from pages.results_page.results_page import ResultsPage
from pages.product_page.product_page import ProductPage
from pages.cart_page.cart_page import CartPage


class TestBuilder:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.loginPage = LoginPage(driver, url)
        self.homePage = HomePage(driver, url)
        self.resultsPage = ResultsPage(driver, url)
        self.productPage = ProductPage(driver, url)
        self.cartPage = CartPage(driver, url)

    def l_login(self, user, password):
        """
        Navigate to login page and login with provided credentials
        :param user: username, str
        :param password: password, str
        :return: self
        """
        self.loginPage.load()
        self.loginPage.login(user, password)

        return self

    def r_search_product(self, product_name):
        """
        Search product
        :param product_name: product name
        :return: self
        """
        self.resultsPage.enter_text_in_search_field(product_name)
        self.resultsPage.click_search()

        return self

    def r_count_products(self, expected_count):
        """
        Count product on results page
        :param expected_count: product count
        :return: self
        """
        self.resultsPage.count_products(expected_count)

        return self

    def p_navigate_to_product(self, url):
        """
        Navigate to product page by url
        :param url: url, str
        :return: self
        """
        self.productPage.navigate_to_page(url)

        return self

    def p_verify_price(self, price):
        """
        Verify product price
        :param price: price, str
        :return: self
        """
        self.productPage.product.verify_price(price)

        return self

    def p_verify_name(self, name):
        """
        Verify product name
        :param name: product name, str
        :return: self
        """
        self.productPage.product.verify_name(name)

        return self

    def p_enter_qty(self, qty):
        """
        Enter product quantity
        :param qty: product quantity, int
        :return: self
        """
        self.productPage.product.enter_qty(qty)

        return self

    def p_select_size(self, size):
        """
        Select product size
        :param size: product size, str
        :return: self
        """
        self.productPage.product.select_size(size)

        return self

    def p_select_color(self, color):
        """
        Select product color
        :param color: product color, str
        :return: self
        """
        self.productPage.product.select_color(color)

        return self

    def p_add_to_cart(self):
        """
        Click button Add to Cart

        :return: self
        """
        self.productPage.product.add_to_cart()

        return self

    def p_verify_title_quantity(self, qty):
        """
        Verify title quantity
        :param qty: product quantity, int
        :return: self
        """
        self.productPage.cart.verify_title_quantity(qty)

        return self

    def c_navigate_to_cart(self):
        """
        Navigate to Cart page
        :return: self
        """
        self.cartPage.load()

        return self

    def c_verify_product_info(self, name, size, color, price, qty, subtotal):
        """
        Verify product price and subtotal on art page
        :param name: product name, str
        :param size: product size, str
        :param color: product color, str
        :param price: product price, str
        :param qty: product qty, str
        :param subtotal: product subtotal, str
        :return: self
        """
        self.cartPage.product.verify_price(name, price)
        self.cartPage.product.verify_size(name, size)
        self.cartPage.product.verify_color(name, color)
        self.cartPage.product.verify_qty(name, qty)
        self.cartPage.product.verify_subtotal(name, subtotal)

        return self

    def c_proceed_to_checkout(self):
        """
        Click Proceed to Checkout
        :return: self
        """
        self.cartPage.click_proceed_to_checkout()

        return self


