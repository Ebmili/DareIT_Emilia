import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button/span[1]"
    login_url = 'https://scouts.futbolkolektyw.pl/en//login'
    polish_login_url = 'https://scouts.futbolkolektyw.pl/en//pl/login'
    expected_title = "Scouts panel - sign in"
    expected_polish_title = "Scouts panel - zaloguj"
    header_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    expected_header_of_box = 'Scouts Panel'
    english_language_listbox_xpath = "//div[2]/div/div"
    polski_option_xpath = "//div[3]/ul/li[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_polish_page(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.polish_login_url) == self.expected_polish_title

    def check_header_of_box(self):
        self.assert_element_text(self.driver, self.header_of_box_xpath, self.expected_header_of_box)

    def click_english_language_listbox(self):
        self.click_on_the_element(self.english_language_listbox_xpath)

    def click_polski_language_option(self):
        self.click_on_the_element(self.polski_option_xpath)

