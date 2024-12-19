"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.home_page.home_page import HomePage
from utils import save_data, log, globl

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


def increase_search_product(searched_product):
    """
    Experimental function to modify searched product
    :param searched_product: , str

    :return: Returns string with 's' at the end
    """
    return str(searched_product) + "s"


def test_01_prepare_testing_data():

    log.message("Preparing test data.")
    products = ["top", "short", "bag", "jacket"]
    new_products = list(map(increase_search_product, products))

    save_data.store(new_products)


def test_02_search_products(driver):

    home_page = HomePage(driver, globl.url)

    products_from_file: list = save_data.exclude()

    log.message("Enter all searched product and click Search.")
    home_page.enter_text_in_search_field(products_from_file[0])
    home_page.click_search()

