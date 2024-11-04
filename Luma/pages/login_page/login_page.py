from selenium.webdriver.common.by import By
from pages.login_page.ComponentContainer import TextBox, Button, ContainerElement
from pages.main.base import BasePage
from utils import verify


class LoginPage(BasePage):

    page_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"

    def __init__(self, driver, url: str):
        super().__init__(driver, url)

        self.username_field = TextBox(driver, (By.ID, "email"))
        self.password_field = TextBox(driver, (By.ID, "pass"))
        self.login_button = Button(driver, (By.XPATH, "//div[@class='login-container']//button[@id='send2']"))
        self.error_message = TextBox(driver, (By.XPATH, "//div[contains(@class, 'message-error')]/div"))

        self.login_container = ContainerElement(
            driver,
            elements=[self.username_field, self.password_field, self.login_button])

    def login(self, username, password):
        """
        Login to site.
        :param username: username
        :param password: password
        """
        self.login_container.enter(username, password)

    def login_and_verify_error(self, username, password, message):
        """
        Enters wrong login credential and verify error message
        :param username: username
        :param password: password
        :param message: error message
        """
        self.login_container.enter(username, password)
        verify.is_equal(self.error_message.find().text, message, f"Error message '{message}' should be displayed.")
