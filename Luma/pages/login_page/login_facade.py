from pages.login_page.login_page import LoginPage
from utils import verify


class LoginFacade:

    def __init__(self, driver, url: str):
        self.__login_page = LoginPage(driver, url)

    def load(self):
        """
        Load Login page
        :return:
        """
        self.__login_page.load()

    def login(self, username, password):
        """
        Login to site.
        :param username: username
        :param password: password
        """
        self.__login_page.username_field.enter(username)
        self.__login_page.password_field.enter(password)
        self.__login_page.login_button.enter()

    def login_and_verify_error(self, username, password, message):
        """
        Enters wrong login credential and verify error message
        :param username: username
        :param password: password
        :param message: error message
        """
        self.login(username, password)

        verify.is_equal(
            self.__login_page.find_element(self.__login_page.error_message.locator).text,
            message,
            f"Error message '{message}' should be displayed.")
