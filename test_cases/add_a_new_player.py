import time
from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from util.settings import IMPLICITLY_WAIT
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium import webdriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestFillingAddPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.get('https://dareit.futbolkolektyw.pl/en/')
        driver.fullscreen_window()
        driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_add_a_player_form(self):
        user_login = LoginPage(driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)

        add_player = AddAPlayer(driver)
        time.sleep(6)
        add_player.type_in_email("jacek@gmail.com")
        add_player.type_in_name("Jacek")
        add_player.type_in_surname("Kopacz")
        add_player.type_in_phone_field("111222333")
        add_player.type_in_age_field("28")
        add_player.type_in_height_field("178")
        add_player.type_in_weight_field("70")
        add_player.type_in_main_position_field("Striker")
        add_player.click_on_the_submit_button()

    @classmethod
    def tearDownClass(cls):
        driver.quit()
