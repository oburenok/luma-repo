from pages.main.base import BasePage
from utils import log


class ProductPage(BasePage):

    page_url = "https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)


