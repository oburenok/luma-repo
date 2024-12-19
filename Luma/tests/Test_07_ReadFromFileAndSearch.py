"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.results_page.results_page import ResultsPage
from utils import log, globl, read_data

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


@pytest.mark.parametrize("test_data", read_data.csv_to_dict("Test_07_ReadFromFileAndSearch.csv"))
def test_01_read_csv_and_search(driver, test_data):

    results_page = ResultsPage(driver, globl.url)

    log.message("Search product.")
    results_page.enter_text_in_search_field(test_data["search_product"])
    results_page.click_search()

    log.message("Verify number of products on the page.")
    results_page.count_products(test_data["found_products_number"])


@pytest.mark.parametrize("test_data", read_data.excel_to_dict('Test_07_ReadFromFileAndSearch.xlsx', 'SearchResults'))
def test_02_read_xlsx_and_search(driver, test_data):

    results_page = ResultsPage(driver, globl.url)

    log.message("Search product.")
    results_page.enter_text_in_search_field(test_data["search_product"])
    results_page.click_search()

    log.message("Verify number of products on the page.")
    results_page.count_products(test_data["found_products_number"])

