import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.dashboard import Dashboard
from pages.login_page import LoginPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.get('https://scouts.futbolkolektyw.pl/en/')
        driver.fullscreen_window()
        driver.get('https://dareit.futbolkolektyw.pl/en/players/add')
        driver.fullscreen_window()

    def test_open_add_a_player_form(self):
        user_login = LoginPage(driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        driver.quit()
