from pages.main.base import BasePage
from selenium.webdriver.common.by import By
from utils import log, verify


class ResultsPage(BasePage):

    page_url = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=Luma"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)

    p_locator = {
        "products_list": ["elem_type", (By.XPATH, "//ol[@class='products list items product-items']/li[@class='item product product-item']")]
    }

    def verify_product(self):
        log.message("Method verify_product() should be defined!!!!")

    def count_products(self, expected_count=None):
        """
        This method counts how many products is displayed on search results page;
        it can also verify if it's expected number or not.

        :param expected_count: Expected number of products
        :type expected_count: str

        :return:
                number of products, int
        Examples:
            s = "hello world"
            verify.equal(s.split(), ['hello', 'world'])
        """
        products_count = len(self.find_elements(self.p_locator["products_list"][1]))

        if expected_count is not None:
            verify.is_equal(str(products_count), expected_count, f"Result page should contains {expected_count} product(s).")

        return products_count




