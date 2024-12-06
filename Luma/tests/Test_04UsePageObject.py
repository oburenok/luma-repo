"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.home_page.home_page import HomePage
from utils import log

# pytestmark = pytest.mark.skipif(pytest.__version__ != '7.3.2', reason='Pytest version is less then 7.3.2')
pytestmark = [pytest.mark.run_every_night]


@pytest.mark.usefixtures("driver")
class Test04UsePageObject:

    # @pytest.mark.integration
    def test_01_use_base_page_object(self):
        self.home_page = HomePage(self.driver, self.url)

        log.message("Search product.")
        self.home_page.enter_text_in_search_field("Tank")
        self.home_page.click_search()

    @pytest.mark.skip(reason="Test contains to much warnings and critical messages.")
    def test_02_navigation_to_google(self):
        self.driver.get("https://www.google.com.ua")
        log.message("bla-bla-bla")
        log.message("Some comments")
        log.message("bla-bla-bla")
        log.message("Some comments")

        log.warning("It is warning message.")
        log.warning("It is warning message.")

        log.message("Add more comments")
        log.message("to simulate testing process.")

        log.critical("Log critical to increase critical counter.")

    @pytest.mark.xfail
    def test_03_failed(self):
        log.message("Test should pass.")
        assert 1 == 0

    @pytest.mark.xfail
    def test_04_failed_pass(self):
        log.message("Test should fail.")
        assert 1 == 1



