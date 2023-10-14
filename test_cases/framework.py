import os
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService

IMPLICITLY_WAIT = 10

class TestMediumPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://medium.com/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = 'Medium – Where good ideas find you.'
        self.assertEqual(actual_title, expected_title)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def tearDown(self):
        self.driver.quit()

