import pytest

from pages.test_builder.test_builder import TestBuilder
from pages.cart_page.cart_page import ProductParam
from utils import globl

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


def test_01_assortment(driver):

    # Defining test data
    product_1 = ProductParam("Sol Active Short",
                             "32",
                             "blue",
                             "32.00",
                             "1",
                             "32.00")

    product_2 = product_1.clone()
    product_2.color = "green"

    product_3 = product_1.clone()
    product_3.color = "purple"

    product_4 = product_1.clone()
    product_4.size = "33"

    product_5 = product_2.clone()
    product_5.size = "34"

    product_6 = product_3.clone()
    product_6.size = "36"

    TestBuilder(driver, globl.url)\
        .p_navigate_to_product("https://magento.softwaretestingboard.com/sol-active-short.html") \
        .p_select_size(product_1.size) \
        .p_select_color(product_1.color) \
        .p_add_to_cart() \
        .p_select_size(product_2.size) \
        .p_select_color(product_2.color) \
        .p_add_to_cart() \
        .p_select_size(product_3.size) \
        .p_select_color(product_3.color) \
        .p_add_to_cart() \
        .p_select_size(product_4.size) \
        .p_select_color(product_4.color) \
        .p_add_to_cart() \
        .p_select_size(product_5.size) \
        .p_select_color(product_5.color) \
        .p_add_to_cart() \
        .p_select_size(product_6.size) \
        .p_select_color(product_6.color) \
        .p_add_to_cart() \
        .p_verify_title_quantity(6) \
        .c_navigate_to_cart() \
        .c_verify_product_info(product_1.name, product_1.size, product_1.color, product_1.price, product_1.qty, product_1.subtotal)

