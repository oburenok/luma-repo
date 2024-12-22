"""
This is a first test for commercial website Luma.
"""

import pytest

from pages.home_page.home_page import HomePage
from utils import log, globl


pytestmark = [pytest.mark.run_every_night]


def test_01_use_base_page_object(driver):
    home_page = HomePage(driver, globl.url)
    home_page.load()

    log.message("Search product.")
    home_page.enter_text_in_search_field("Tank")
    home_page.click_search()


@pytest.mark.skip(reason="Test contains to much warnings and critical messages.")
def test_02_navigation_to_google():
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
def test_03_failed():
    log.message("Test should pass.")
    assert 1 == 0


@pytest.mark.xfail
def test_04_failed_pass():
    log.message("Test should fail.")
    assert 1 == 1



