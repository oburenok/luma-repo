"""
This is a test for commercial website Luma.
"""

import time
import pytest

from pages.home_page.home_page import HomePage
from pages.results_page.results_page import ResultsPage
from utils import log

pytestmark = [pytest.mark.integration, pytest.mark.sanity]


@pytest.mark.usefixtures("driver")
class Test05UsePageObject:

    @pytest.mark.sanity
    def test_01_use_base_page_object(self):
        self.home_page = HomePage(self.driver, self.url)

        log.message("Search product.")
        self.home_page.enter_text_in_search_field("Bag")
        self.home_page.click_search()

        log.message("Navigate to category menus.")
        self.home_page.category_menu.navigate_to_category("woman wtops wjackets")
        time.sleep(1)

        self.home_page.category_menu.navigate_to_category("man mtops mtees", click=False)
        time.sleep(1)

        self.home_page.category_menu.navigate_to_category("gear fitnessequipment")
        time.sleep(1)

    @pytest.mark.smoke
    def test_02_navigation_to_google(self):
        self.results_page = ResultsPage(self.driver, self.url)

        log.message("Search product.")
        self.results_page.enter_text_in_search_field("Watch")
        self.results_page.click_search()
        time.sleep(2)

        log.step("1.001", "Verify product.")
        self.results_page.verify_product()

        log.step("1.002", "Count products on results page.")
        self.results_page.count_products(5)


