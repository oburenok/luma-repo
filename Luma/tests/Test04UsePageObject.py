"""
This is a first test for commercial website Luma.
"""

import time
import pytest

from pages.main.base import BasePage
from utils import log


@pytest.mark.usefixtures("driver")
class Test04UsePageObject:

    def test_01_use_base_page_objet(self):
        self.home_page = BasePage(self.driver, "https://magento.softwaretestingboard.com/what-is-new.html")

        log.message("Search product.")
        self.home_page.enter_text_in_search_field("Tank")
        self.home_page.click_search()

        time.sleep(4)

    # def test_navigation_to_google(self):
    #     self.driver.get("https://www.google.com.ua")
    #     log.message("bla-bla-bla")
    #     log.message("Some comments")
    #     log.message("bla-bla-bla")
    #     log.message("Some comments")
    #
    #     log.warning("It is warning message.")
    #     log.warning("It is warning message.")
    #
    #     log.message("Add more comments")
    #     log.message("to simulate testing process.")
    #
    #     log.critical("Log critical to increase critical counter.")
    #     time.sleep(1.5)

