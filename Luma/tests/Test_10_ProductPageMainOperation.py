"""
This is a first test for commercial website Luma.
"""
import pytest

from pages.product_page.product_page import ProductPage
from utils import log, globl, read_data

pytestmark = [pytest.mark.integration]


@pytest.mark.parametrize(
    "test_data",
    read_data.excel_to_dict('Test_10_ProductPageMainOperation.xlsx', 'ProductPage_1'))
def test_01_verify_adding_product_to_cart(driver, test_data):

    product_page = ProductPage(driver, globl.url)

    product_page.navigate_to_page(test_data["product_page"])

    log.step("1.001", "Verify product name.")
    product_page.product.verify_name(test_data["name"])

    log.step("1.002", "Verify product price.")
    product_page.product.verify_price(test_data["price"])

    log.step("1.003", "Verify default product quantity.")
    product_page.product.verify_qty(test_data["quantity"])

    log.step("1.004", "Choose size S and color green")
    product_page.product.select_size(test_data["size"])
    product_page.product.select_color(test_data["color"])

    log.step("1.005", "Enter product quantity.")
    product_page.product.enter_qty(test_data["enter_qty"])

    log.step("1.005", "Adding product to the cart.")
    product_page.product.add_to_cart()

    log.step("1.006", "Verify cart title quantity.")
    product_page.cart.verify_title_quantity(test_data["title_qty"])

