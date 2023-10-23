from lib2to3.pgen2 import driver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_xpath = "//*[text()='Add player']"
    email_field_xpath = "//input[@name = 'email']"
    name_field_xpath = "//input[@name = 'name']"
    surname_field_xpath = "//input[@name = 'surname']"
    phone_field_xpath = "//input[@name = 'phone']"
    weight_field_xpath = "//input[@name = 'weight']"
    height_field_xpath = "//input[@name = 'height']"
    age_field_xpath = "//input[@name = 'age']"
    main_position_field_xpath = "//input[@name = 'mainPosition']"
    submit_button_xpath = "//button[@type='submit']"
    add_player_title = "Add player"
    player_form_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    player_title_xpath = "/html/head/title"
    clear_button_xpath = "//div[3]/button[2]/span[1]"
    wait = WebDriverWait(driver, 10)
    required_message_xpath = "//p[contains(@class, 'required')]"

    def check_title_of_page(self):
        self.click_on_the_element(self.add_player_xpath)
        self.wait_for_element_to_be_clickable(self.add_player_xpath)
        assert self.get_page_title(self.player_title_xpath) == self.add_player_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone_field(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight_field(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height_field(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age_field(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position_field(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def required_message(self):
        self.visibility_of_element_located(self.required_message_xpath)
        assert (self.driver, self.required_message_xpath, "Required")
