from selenium.webdriver.remote.webdriver import WebDriver
from abc import ABC, abstractmethod

from utils import log


class BaseElement(ABC):

    def __init__(self, driver: WebDriver, locator: tuple):
        self.driver = driver
        self.locator = locator

    def find(self):
        return self.driver.find_element(*self.locator)

    @abstractmethod
    def enter(self, *args):
        """This method should enter data or click buttons"""
        pass


class Button(BaseElement):

    def enter(self):
        """
        Clicks the button
        """
        self.find().click()


class TextBox(BaseElement):

    def enter(self, text=""):
        """
        Entering text in field
        :param text: text
        """
        log.message(f"Entering text '{text}' into the text box")
        elem_field = self.find()

        elem_field.clear()
        elem_field.send_keys(text)


class ContainerElement(BaseElement):
    def __init__(self, driver: WebDriver, elements: list[BaseElement]):
        self.driver = driver
        self.elements = elements

    def enter(self, *args):
        """
        Calling all elements and their methods enter(), to input data in the fields.
        :param args:
        :return:
        """
        log.message("Entering data for elements in Container.")

        for i, element in enumerate(self.elements):

            if i < len(args):
                element.enter(args[i])
            else:
                element.enter()

