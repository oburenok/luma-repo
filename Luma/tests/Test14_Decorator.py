"""
Test for decorator.
"""
import pytest

from pages.cart_page.cart_page import CartPage
from utils import log, decorators

pytestmark = [pytest.mark.run_every_night, pytest.mark.quick]


PI_NUMBER = 3.1415926
string_variable = "Test string for global variable."


@pytest.mark.usefixtures("driver")
class Test14Decorator:
    """Testing decorator 'stopwatch'."""

    @decorators.stopwatch
    def test_01_decorator(self):
        """Testing decorator 'stopwatch'."""
        global PI_NUMBER, string_variable

        self.cartPage = CartPage(self.driver, self.url)

        log.message("Navigate to Cart page.")
        self.cartPage.load()

        log.message(string_variable)

        string_variable = "String is updated."
        log.message(string_variable)
        log.message(PI_NUMBER)
