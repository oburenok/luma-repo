"""
This is a Login test for commercial website Luma.
"""

import pytest

from pages.login_page.login_page import LoginPage
from utils import log, globl

pytestmark = [pytest.mark.run_every_night, pytest.mark.integration]


def test_01_logging(driver):

    login_page = LoginPage(driver, globl.url)

    log.message("Logging to the site Luma and verify error.")
    login_page.load()
    login_page.login_and_verify_error("invalid@gmail.com", "qwerty12345",
                                          "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")

    log.message("Logging to the site Luma.")
    login_page.load()
    login_page.login("User1@gmail.com", "qwerty12345")

