"""
This is EXPERIMENTAL TEST for Shadow DOM elements, and it is not actually related to Test Framework.
"""
import pytest

from selenium.webdriver.common.by import By
from pages.product_page.product_page import ProductPage
from utils import log, globl

pytestmark = [pytest.mark.integration]


def test_01_verify_default_product_info(driver):

    log.message("Navigate to tested webpage.")
    web_page = "https://letcode.in/shadow"
    product_page = ProductPage(driver, globl.url)
    product_page.navigate_to_page(web_page, close_footer_ads=False)

    log.message("Enter text in the field in Shadow DOM (open).")
    shadow_host = driver.find_element(By.XPATH, "//div[@id='open-shadow']")
    elem = shadow_host.shadow_root.find_element(By.CSS_SELECTOR, 'input[id="fname"]')
    elem.send_keys("my name")

    log.message("Enter text in the field in Shadow DOM (closed). Reopen Shadow DOM by CDP")
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
    Element.prototype._attachShadow = Element.prototype.attachShadow;
    Element.prototype.attachShadow = function () {
        return this._attachShadow( { mode: "open" } );
    };
    """})
    driver.get(web_page)

    shadow_host = driver.find_element(By.XPATH, "//div[@id='close-shadow']")
    elem = shadow_host.shadow_root.find_element(By.CSS_SELECTOR, 'input[id="email"]')
    elem.send_keys("my email")

