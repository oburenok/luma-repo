"""
This is a Login test for commercial website Luma.
"""

import pytest

from pages.results_page.results_page import ResultsPage
from pages.login_page.login_page import LoginPage
from utils import log


@pytest.mark.usefixtures("driver")
class Test08LoginComposite:

    def test_01_logging(self):

        self.results_page = ResultsPage(self.driver, self.url)
        self.loginPage = LoginPage(self.driver, self.url)

        log.message("Logging to the site Luma and verify error.")
        self.loginPage.load()
        self.loginPage.login_and_verify_error("invalid@gmail.com", "qwerty12345",
                                              "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")

        log.message("Logging to the site Luma.")
        self.loginPage.load()
        self.loginPage.login("User1@gmail.com", "qwerty12345")

