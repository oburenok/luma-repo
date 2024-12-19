"""
This is a test for commercial website Luma.
"""

import pytest

from pages.home_page.home_page import HomePage
from pages.results_page.results_page import ResultsPage
from utils import log, globl

pytestmark = [pytest.mark.integration, pytest.mark.sanity]


@pytest.mark.sanity
def test_01_use_base_page_object(driver):
    home_page = HomePage(driver, globl.url)

    log.message("Search product.")
    home_page.enter_text_in_search_field("Bag")
    home_page.click_search()

    log.message("Navigate to category menus.")
    home_page.category_menu.navigate_to_category("woman wtops wjackets")

    home_page.category_menu.navigate_to_category("man mtops mtees", click=False)

    home_page.category_menu.navigate_to_category("gear fitnessequipment")


@pytest.mark.smoke
def test_02_navigation_to_google(driver):
    results_page = ResultsPage(driver, globl.url)

    log.message("Search product.")
    results_page.enter_text_in_search_field("Watch")
    results_page.click_search()

    log.step("1.001", "Verify product.")
    results_page.verify_product()

    log.step("1.002", "Count products on results page.")
    results_page.count_products('9')


