from pages.main.base import BasePage
from utils import log


class HomePage(BasePage):

    page_url = "https://magento.softwaretestingboard.com/"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)


