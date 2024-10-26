"""
This is a first test for commercial website Luma.
"""

import time
import pytest

from pages.results_page.results_page import ResultsPage
from utils import log


@pytest.mark.usefixtures("driver")
class Test06ParametrizeSearch:

    @pytest.mark.parametrize('product, counter', [('bag', 10), ('tshirt', 0), ('watch', 9)])
    def test_01_use_base_page_object(self, product, counter):
        self.results_page = ResultsPage(self.driver, self.url)

        log.message("Search product.")
        self.results_page.enter_text_in_search_field(product)
        self.results_page.click_search()

        log.message("Verify number of products.")
        self.results_page.count_products(counter)

        log.message("Update to make Jenkins start build after this commit.")

