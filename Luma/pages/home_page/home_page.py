from pages.main.base import BasePage
from utils import log


class HomePage(BasePage):

    def __init__(self, driver, url: str):
        super().__init__(driver, url)

