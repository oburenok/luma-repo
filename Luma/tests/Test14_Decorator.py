"""
Test for decorator.
"""
import pytest

from pages.cart_page.cart_page import CartPage
from utils import log, decorators


STRING_VARIABLE = "Test string for global variable."


@pytest.mark.usefixtures("driver")
class Test14Decorator:
    """Testing decorator 'stopwatch'."""

    @decorators.stopwatch
    def test_01_decorator(self):
        """Testing decorator 'stopwatch'."""
        global STRING_VARIABLE

        self.cartPage = CartPage(self.driver, self.url)

        log.message("Navigate to Cart page.")
        self.cartPage.load()

        log.message(STRING_VARIABLE)

        STRING_VARIABLE = "String is updated."
        log.message(STRING_VARIABLE)
