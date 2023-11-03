from lib2to3.pgen2 import driver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import time


class Dashboard(BasePage):
    add_player_xpath = "//*[text()= 'Add player']"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    polski_button_xpath = "//*[text()= 'Polski']"
    players_button_xpath = "//*[text()= 'Players']"
    last_player_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//div[3]/div/div/a[2]/button/span[1]"
    last_updated_match_xpath = "//div[3]/div/div/a[4]/button/span[1]"
    last_updated_report = "//div[3]/div/div/a[5]/button/span[1]"
    last_created_match_xpath = "//div[3]/div/div/a[3]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://dareit.futbolkolektyw.pl/en/"
    add_player_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    add_player_title = "Add player"
    futbol_kolektyw_button_xpath = '//*[@title = "Logo Scouts Panel"]'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_xpath)

    def add_a_player_form(self):
        self.click_on_the_element(self.add_player_xpath)
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.add_player_title

    def click_on_the_sign_out_button(self):
        time.sleep(5)
        self.click_on_the_element(self.sign_out_button_xpath)

pass
