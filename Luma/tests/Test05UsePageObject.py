"""
This is a test for commercial website Luma.
"""

import time
import pytest

from pages.main.base import BasePage
from utils import log


@pytest.mark.usefixtures("driver")
class Test05UsePageObject:

    @pytest.mark.sanity
    def test_01_use_base_page_object(self):
        self.home_page = BasePage(self.driver, "https://magento.softwaretestingboard.com/what-is-new.html")

        log.message("Search product.")
        self.home_page.enter_text_in_search_field("Bag")
        self.home_page.click_search()

        log.message("Navigate to category menus.")
        self.home_page.category_menu.navigate_to_category("woman wtops wjackets")
        time.sleep(2)

        self.home_page.category_menu.navigate_to_category("man mtops mtees", click=False)
        time.sleep(2)

        self.home_page.category_menu.navigate_to_category("gear fitnessequipment")
        time.sleep(2)

    # @pytest.mark.skip()
    # def test_02_navigation_to_google(self):
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
    #     # log.critical("Log critical to increase critical counter.")
    #     # time.sleep(1.5)

