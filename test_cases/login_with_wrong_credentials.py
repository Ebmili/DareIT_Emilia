import unittest
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium import webdriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver.get('https://scouts.futbolkolektyw.pl/en/')
        driver.fullscreen_window()

    def test_log_in_to_the_system(self):
        user_login = LoginPage(driver)
        user_login.title_of_page()
        user_login.check_header_of_box()
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()

    def test_log_in_with_invalid_data(self):
        user_login = LoginPage(driver)
        user_login.title_of_page()
        user_login.check_header_of_box()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234567')
        user_login.click_sign_in_button()
        user_login.check_invalid_password_message()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

