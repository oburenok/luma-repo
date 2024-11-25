import pytest

from pages.cart_page.cart_page import CartPage
from utils import log, decorators


@pytest.mark.usefixtures("driver")
class Test14Decorator:

    @decorators.stopwatch
    def test_01_decorator(self):
        self.cartPage = CartPage(self.driver, self.url)

        log.message("Navigate to Cart page.")
        self.cartPage.load()

