"""
This module contains all methods which reads/fetches configuration settings for automation.
"""

import configparser
import os
import sys
import inspect

from utils import globl


class GetConfig:
    """
    This class allows to fetch all configuration
    setting from standart_env_config.ini file
    """

    def __init__(self):
        globl.project_name = 'Luma'  # This is constant variable
        self.get_project_path(os.getcwd())
        self.config = configparser.ConfigParser()
        self.config.read(globl.project_path + '\\config\\standart_env_config.ini')

    def get_project_path(self, path):
        """
        This method searches project path
        :param path:  of current directory
        :type path: str

        :return:
                str: path to project
        """
        len_name = len(globl.project_name)

        if path[-len_name:] == globl.project_name:
            globl.project_path = path
            return True
        else:
            path = os.path.split(path)[0]
            self.get_project_path(path)

    def read_all_sections(self):
        self.read_environment_section()
        # self.read_test_section()
        self.read_project_section()

    def read_environment_section(self):
        """
        Call this method to read all settings
        from section [Environment]
        """

        globl.host = self.config['Environment']['host']
        globl.url = self.config['Environment']['url']
        globl.browser = self.config['Environment']['browser']

    def read_test_section(self):
        """
        Call this method to read all settings
        from section [Test]
        """

        globl.test_name = self.config['Test']['test_name']

    def read_project_section(self):
        """
        Call this method to read all settings
        from section [Project]
        """

        globl.reports_path = globl.project_path + '\\reports'
        globl.test_path = os.getcwd()
