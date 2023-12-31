"""
This file defines how to start web browser and what browser will be started.
At this moment, three different browser can be started:
    Chrome, Firefox, Edge
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FFService

from utils import log


class RunBrowser:
    """
    This class starting browser according to configuration defined
    in config.standart_env_config.ini file
    """
    def __init__(self, browser, url):
        self.url = url
        self.driver = None
        self.init_browser(browser)

    def init_browser(self, browser):
        """
        This method starting browser and navigate to starting page
        :return:
        """
        log.message(f"Starting browser '{browser}'.")
        browse_drivers = {'chrome': self.run_chrome,
                          'firefox': self.run_firefox,
                          'edge': self.run_edge}

        self.driver = browse_drivers[browser]()

        log.message(f"Navigating to start page: {self.url}")
        self.driver.get(self.url)
        self.driver.maximize_window()

    def run_firefox(self):
        """
        This method starting up Firefox browser
        :return:
                Browse WebDriver
        """
        ff_service = FFService(executable_path="C:\\Users\\oburenok\\PycharmProjects\\Luma" +
                                               "\\drivers\\firefox\\geckodriver.exe")
        driver = webdriver.Firefox(service=ff_service)

        return driver

    def run_edge(self):
        """
        This method starting up Edge browser
        :return:
                Browse WebDriver
        """
        edge_service = EdgeService(
            executable_path="C:\\Users\\oburenok\\PycharmProjects\\Luma\\drivers" +
                            "\\edge\\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

        return driver

    def run_chrome(self):
        """
        This method starting up Chrome browser
        :return:
                Browse WebDriver
        """
        chrome_service = ChromeService(
            executable_path="C:\\Users\\oburenok\\PycharmProjects\\Luma\\drivers" +
                            "\\chrome\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)

        return driver
