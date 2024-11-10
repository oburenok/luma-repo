import time
import pytest

from pages.product_page.product_page import ProductPage
from utils import log, read_data


@pytest.mark.usefixtures("driver")
class Test10ProductPageMainOperation:

    @pytest.mark.parametrize(
        "test_data",
        read_data.excel_to_dict('Test10_ProductPageMainOperation.xlsx', 'ProductPage_1'))
    def test_01_verify_adding_product_to_cart(self, test_data):

        self.productPage = ProductPage(self.driver, self.url)

        self.productPage.navigate_to_page(test_data["product_page"])

        log.step("1.001", "Verify product name.")
        self.productPage.product.verify_name(test_data["name"])

        log.step("1.002", "Verify product price.")
        self.productPage.product.verify_price(test_data["price"])

        log.step("1.003", "Verify default product quantity.")
        self.productPage.product.verify_qty(test_data["quantity"])

        log.step("1.004", "Choose size S and color green")
        self.productPage.product.select_size(test_data["size"])
        self.productPage.product.select_color(test_data["color"])

        log.step("1.005", "Enter product quantity.")
        self.productPage.product.enter_qty(test_data["enter_qty"])

        log.step("1.005", "Adding product to the cart.")
        self.productPage.product.add_to_cart()

        log.step("1.006", "Verify cart title quantity.")
        self.productPage.cart.verify_title_quantity(test_data["title_qty"])

        time.sleep(2)
