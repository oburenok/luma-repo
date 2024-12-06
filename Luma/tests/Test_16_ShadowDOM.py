"""
This is more experimental test for Shadow DOM elements, and it is not actually related to Test Framework.
"""
import pytest
import time

from selenium.webdriver.common.by import By
from pages.product_page.product_page import ProductPage
from utils import log

pytestmark = [pytest.mark.integration]


@pytest.mark.usefixtures("driver")
class Test16ShadowDOM:

    def test_01_verify_default_product_info(self):

        log.message("Navigate to tested webpage.")
        web_page = "https://letcode.in/shadow"
        self.productPage = ProductPage(self.driver, self.url)
        self.productPage.navigate_to_page(web_page, close_footer_ads=False)

        log.message("Enter text in the field in Shadow DOM (open).")
        shadow_host = self.driver.find_element(By.XPATH, "//div[@id='open-shadow']")
        elem = shadow_host.shadow_root.find_element(By.CSS_SELECTOR, 'input[id="fname"]')
        elem.send_keys("my name")

        time.sleep(1.5)

        log.message("Enter text in the field in Shadow DOM (closed). Reopen Shadow DOM by CDP")
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
        Element.prototype._attachShadow = Element.prototype.attachShadow;
        Element.prototype.attachShadow = function () {
            return this._attachShadow( { mode: "open" } );
        };
        """})
        self.driver.get(web_page)

        shadow_host = self.driver.find_element(By.XPATH, "//div[@id='close-shadow']")
        elem = shadow_host.shadow_root.find_element(By.CSS_SELECTOR, 'input[id="email"]')
        elem.send_keys("my email")

        time.sleep(1.5)

