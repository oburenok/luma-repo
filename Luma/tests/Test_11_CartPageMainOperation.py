"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.product_page.product_page import ProductPage
from pages.cart_page.cart_page import CartPage
from utils import log, globl, read_data

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


@pytest.mark.order(20)
def test_02_navigate_to_cart_page(driver):

    cart_page = CartPage(driver, globl.url)

    log.step("2.001", "Navigate to Cart page")
    cart_page.load()


@pytest.mark.order(30)
@pytest.mark.parametrize(
    "test_data",
    read_data.excel_to_dict('Test_11_CartPageMainOperation.xlsx', 'CartPage_1'))
def test_03_verify_product_in_cart(driver, test_data):

    cart_page = CartPage(driver, globl.url)

    log.step("3.001", "Verify product 'Zoe Tank' present in the cart.")
    cart_page.product.verify_name(test_data["name"])

    log.step("3.002", "Verify product size and color.")
    cart_page.product.verify_size(test_data["name"], test_data["size"])
    cart_page.product.verify_color(test_data["name"], test_data["color"])

    log.step("3.003", "Verify product Price and Subtotal.")
    cart_page.product.verify_price(test_data["name"], test_data["price"])
    cart_page.product.verify_subtotal(test_data["name"], test_data["subtotal"])

    log.step("3.004", "Verify product quantity.")
    cart_page.product.verify_qty(test_data["name"], test_data["qty"])

    log.step("3.005", "Enter new product quantity.")
    cart_page.product.enter_qty(test_data["name"], test_data["enter_qty"])


@pytest.mark.order(40)
def test_04_click_proceed_to_checkout(driver):

    cart_page = CartPage(driver, globl.url)

    log.step("4.001", "Click to button Proceed to Checkout")
    cart_page.click_proceed_to_checkout()


@pytest.mark.order(10)
@pytest.mark.parametrize(
    "test_data",
    read_data.excel_to_dict('Test_11_CartPageMainOperation.xlsx', 'ProductPage_1'))
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

