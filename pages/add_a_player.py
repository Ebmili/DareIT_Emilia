import time

from pages.base_page import BasePage
from faker import Faker


class AddAPlayer(BasePage):
    page_title_xpath = "//header//h6"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_option_xpath = "//div[3]/ul/li[1]"
    left_leg_option_xpath = "//div[3]/ul/li[2]"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    district_xpath_map = {
        "Lower Silesia": "//li[1]",
        "Kuyavia-Pomerania": "//li[2]",
        "Lublin": "//li[3]",
        "Lubusz": "//li[4]",
        "Łódź": "//li[5]",
        "Lesser Poland": "//li[6]",
        "Masovia": "//li[7]",
        "Opole": "//li[8]",
        "Subcarpathia": "//li[9]",
        "Podlaskie": "//li[10]",
        "Pomerania": "//li[11]",
        "Silesia": "//li[12]",
        "Holy Cross Province": "//li[13]",
        "Warmia-Masuria": "//li[14]",
        "Greater Poland": "//li[15]",
        "West Pomerania": "//li[16]"

    }
    achievements_field_xpath = "//input[@name='achievements']"
    add_lang_button_xpath = "//button[@aria-label='Add language']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[@type='submit']//following-sibling::button"
    progress_bar_toaster_xpath = "//*[@role='alert']"
    add_a_player_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = 'Add player'
    name = ""
    surname = ""
    expected_title_player_added = " "

    def type_in_email(self):
        fake = Faker()
        email = fake.email()
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self):
        fake = Faker()
        self.name = fake.name()
        self.field_send_keys(self.name_field_xpath, self.name)

    def type_in_surname(self):
        fake = Faker()
        self.surname = fake.last_name()
        self.field_send_keys(self.surname_field_xpath, self.surname)

    def type_in_phone(self):
        fake = Faker()
        phone = fake.phone_number()
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self):
        fake = Faker()
        weight = fake.random_int(min=50, max=150)
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self):
        fake = Faker()
        height = fake.random_int(min=150, max=200)
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self):
        fake = Faker()
        age = fake.date()
        self.field_send_keys(self.age_field_xpath, age)

    def select_leg(self):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)
        fake = Faker()
        leg = fake.random_element(elements=('left', 'right'))
        if leg == "left":
            self.wait_for_element_to_be_clickable(self.left_leg_option_xpath)
            self.click_on_the_element(self.left_leg_option_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.right_leg_option_xpath)
            self.click_on_the_element(self.right_leg_option_xpath)

    def type_in_club(self):
        fake = Faker()
        club = fake.text()
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level(self):
        fake = Faker()
        level = fake.text()
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_main_position(self):
        fake = Faker()
        main_position = fake.job()
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self):
        fake = Faker()
        second_position = fake.job()
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def select_district(self):
        fake = Faker()
        district = fake.random_element(
            elements=('Lower Silesia', 'Pomerania', 'Masovia' 'Lublin', 'Lubusz', 'Łódź', 'Kuyavia-Pomerania'
                                                                                          'Lesser Poland', 'Opole',
                      'Subcarpathia', 'Silesia', 'Podlaskie', 'Holy Cross Province', 'Warmia-Masuria', 'Greater Poland',
                      'West Pomerania'))
        self.wait_for_element_to_be_clickable(self.district_field_xpath)
        self.click_on_the_element(self.district_field_xpath)
        xpath = self.district_xpath_map.get(district)
        if xpath:
            self.wait_for_element_to_be_clickable(xpath)
            self.click_on_the_element(xpath)

    def type_in_achievements(self):
        fake = Faker()
        achievements = fake.text()
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert test_title == self.expected_title

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.progress_bar_toaster_xpath)
        player_title = self.driver.title
        self.expected_title_player_added = f"Edit player {self.name} {self.surname}"
        assert player_title == self.expected_title_player_added