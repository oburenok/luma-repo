"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.results_page.results_page import ResultsPage
from utils import log, read_data


@pytest.mark.usefixtures("driver")
class Test07ReadFromFileAndSearch:

    # def test_00_get_test_data(self):
    #     self.test_data = read_data.excel_to_dict('Test07_ReadFromFileAndSearch.xlsx',
    #                                              ['SearchResults', 'HomePage'])

    @pytest.mark.parametrize("test_data", read_data.csv_to_dict("Test07_ReadFromFileAndSearch.csv"))
    def test_01_read_csv_and_search(self, test_data):

        self.results_page = ResultsPage(self.driver, self.url)

        log.message("Search product.")
        self.results_page.enter_text_in_search_field(test_data["search_product"])
        self.results_page.click_search()

        log.message("Verify number of products.")
        self.results_page.count_products(test_data["found_products_number"])

