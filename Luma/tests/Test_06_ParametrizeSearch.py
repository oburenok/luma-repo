"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.results_page.results_page import ResultsPage
from utils import log, globl

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


@pytest.mark.parametrize('product, counter', [('bag', '10'), ('tshirt', '0'), ('watch', '9')])
def test_01_use_base_page_object(driver, product, counter):
    results_page = ResultsPage(driver, globl.url)

    log.message("Search product.")
    results_page.enter_text_in_search_field(product)
    results_page.click_search()

    log.message("Verify number of products.")
    results_page.count_products(counter)

    log.message("Update to make Jenkins start build after this commit.")

