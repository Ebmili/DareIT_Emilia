import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer
from PIL import Image


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        filled_player_file_path = os.path.abspath("screenshots/add_a_new_player/filled_player.png")
        added_player_file_path = os.path.abspath("screenshots/add_a_new_player/added_player.png")
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_add_a_player_button()
        add_a_player = AddAPlayer(self.driver)
        add_a_player.title_of_page()
        add_a_player.type_in_email()
        add_a_player.type_in_name()
        add_a_player.type_in_surname()
        add_a_player.type_in_phone()
        add_a_player.type_in_weight()
        add_a_player.type_in_height()
        add_a_player.type_in_age()
        add_a_player.select_leg()
        add_a_player.type_in_club()
        add_a_player.type_in_level()
        add_a_player.type_in_main_position()
        add_a_player.type_in_second_position()
        add_a_player.select_district()
        add_a_player.type_in_achievements()
        add_a_player.click_submit_button()
        self.driver.save_screenshot(filled_player_file_path)
        Image.open(filled_player_file_path).show()
        add_a_player.player_added_title_of_the_page()
        self.driver.save_screenshot(added_player_file_path)
        Image.open(added_player_file_path).show()

    @classmethod
    def tearDown(self):
        self.driver.quit()