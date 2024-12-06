"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.results_page.results_page import ResultsPage
from utils import log, read_data, start_browser


@pytest.mark.usefixtures("driver")
class Test09SingletonWebDriver:

    @pytest.mark.parametrize("test_data", read_data.excel_to_dict('Test_09_SingletonWebDriver.xlsx', 'SearchResults1'))
    def test_01_driver_by_default(self, test_data):
        log.message("CURRENT WebDRIVER IS:")
        log.message(self.driver)

        self.results_page = ResultsPage(self.driver, self.url)

        log.message("Search product.")
        self.results_page.enter_text_in_search_field(test_data["search_product"])
        self.results_page.click_search()

        log.message("Verify number of products on the page.")
        self.results_page.count_products(test_data["found_products_number"])

    @pytest.mark.parametrize("test_data", read_data.excel_to_dict('Test_09_SingletonWebDriver.xlsx', 'SearchResults2'))
    def test_02_new_driver_instance(self, test_data):
        log.message("Create new instance of WebDriver.")
        new_instance = start_browser.RunBrowser("chrome", self.url)

        log.message("NEW WebDRIVER IS:")
        log.message(new_instance.driver)
        log.message("Existed and created drivers are the same?")
        log.message(self.driver == new_instance.driver)

        self.driver = new_instance.driver

        self.results_page = ResultsPage(self.driver, self.url)

        log.message("Search product.")
        self.results_page.enter_text_in_search_field(test_data["search_product"])
        self.results_page.click_search()

        log.message("Verify number of products on the page.")
        self.results_page.count_products(test_data["found_products_number"])

