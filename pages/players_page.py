from pages.base_page import BasePage


class PlayersPage(BasePage):
    players_page_url = 'https://scouts.futbolkolektyw.pl/en//en/players'
    download_csv_button_xpath = '//*[@title="Download CSV"]'
    print_button_xpath = '//*[@title="Print"]'
    view_columns_button_xpath = '//*[@title="View Columns"]'
    filter_table_button_xpath = '//*[@title="Filter Table"]'
    filter_table_name_field_xpath = '//*/label [text() = "Name"]/parent::div/div/input'
    filter_table_surname_field_xpath = '//*/label [text() = "Surname"]/parent::div/div/input'
    filter_table_age_min_field_xpath = '//label [text()="Age"]/parent::div/div/div[1]//input'
    filter_table_age_max_field_xpath = '//label [text()="Age"]/parent::div/div/div[2]//input'
    filter_table_main_position_field_xpath = '//*/label [text() = "Main position"]/parent::div/div/input'
    filter_table_club_field_xpath = '//*/label [text() = "Club"]/parent::div/div/input'
    filter_table_rate_min_field_xpath = '//label [text()="Rate"]/parent::div/div/div[1]//input'
    filter_table_rate_max_field_xpath = '//label [text()="Rate"]/parent::div/div/div[2]//input'
    filter_table_close_button_xpath = '//*[@aria-label ="Close"]'
    result_table_xpath = '//body'
    name_column_xpath = '//*[@id="MUIDataTableBodyRow-0"]/td[1]'
    surname_column_xpath = '//*[@id="MUIDataTableBodyRow-0"]/td[2]'
    main_position_column_xpath = '//*[@id="MUIDataTableBodyRow-0"]/td[4]'
    first_line_table_xpath = '//*[@id="MUIDataTableBodyRow-0"]'

    def click_filter_button(self):
        self.click_on_the_element(self.filter_table_button_xpath)

    def type_in_name_field(self, name):
        self.field_send_keys(self.filter_table_name_field_xpath, name)

    def check_text_to_be_present_in_element(self, text):
        self.wait_for_text_to_be_present_in_element(text, self.result_table_xpath)

    def click_close_filter_button(self):
        self.click_on_the_element(self.filter_table_close_button_xpath)

    def type_in_surname_field(self, surname):
        self.field_send_keys(self.filter_table_surname_field_xpath, surname)

    def type_in_main_position_field(self, main_position):
        self.field_send_keys(self.filter_table_main_position_field_xpath, main_position)

    def wait_for_text_to_be_present_in_element(self, text, result_table_xpath):
        pass
