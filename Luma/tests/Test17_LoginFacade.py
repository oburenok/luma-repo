"""
This is a Login test uses Login Facade.
"""
import pytest

from pages.login_page.login_facade import LoginFacade
from utils import log


@pytest.mark.usefixtures("driver")
class Test17LoginFacade:

    def test_01_logging(self):
        self.login_facade = LoginFacade(self.driver, self.url)

        log.step("1.001", "Naigate to Login page.")
        self.login_facade.load()

        log.message("Logging to the site Luma and verify error.")
        self.login_facade.login_and_verify_error("invalid@gmail.com", "qwerty12345",
                                              "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")

        log.step("1.002", "Logging to the site Luma.")
        self.login_facade.load()
        self.login_facade.login("User1@gmail.com", "qwerty12345")

