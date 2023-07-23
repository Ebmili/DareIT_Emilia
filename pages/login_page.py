import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[starts-with(@class,'MuiButtonBase-root')]"
    remind_password_xpath = "//a[starts-with(@class,'MuiTypography-root')]"
    language_selection_xpath = "/html/body/div/form/div/div[2]/div/input"
    title_scouts_panel_xpath = "//h5[starts-with(@class, 'MuiTypography-root')]"
    title_of_box_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    header_of_box = 'Scouts Panel'
    add_a_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = 'Scouts panel - sign in'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_page_title(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)