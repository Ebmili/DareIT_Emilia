import time

from util.settings import IMPLICITLY_WAIT

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import unittest

from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.get('https://dareit.futbolkolektyw.pl/en/')
        driver.fullscreen_window()
        driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)

        add_player = AddAPlayer(driver)
        time.sleep(6)

        add_player.type_in_email()
        add_player.type_in_name()
        add_player.type_in_surname()
        add_player.type_in_phone()
        add_player.type_in_weight()
        add_player.type_in_height()
        add_player.type_in_age()
        add_player.select_leg()
        add_player.type_in_club()
        add_player.type_in_level()
        add_player.type_in_main_position()
        add_player.type_in_second_position()
        add_player.select_district()
        add_player.type_in_achievements()
        add_player.click_submit_button()

        driver.save_screenshot('screenshot.png')
