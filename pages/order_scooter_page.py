import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage


class OrderScooterPage(BasePage):
    #  Первая форма заказа самоката
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    underground_station_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    uderground_station_dropdown = [By.XPATH, "//div[@class='select-search__select']"]
    phone_number_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    continue_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']"]

    #  Вторая форма заказа самоката
    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    leasing_period_dropdown = [By.XPATH, "//div[@class='Dropdown-control']"]
    dropdown_1day_leasing = [By.XPATH, "//div[@class='Dropdown-option'][1]"]
    dropdown_2days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][2]"]
    dropdown_3days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][3]"]
    dropdown_4days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][4]"]
    dropdown_5days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][5]"]
    dropdown_6days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][6]"]
    dropdown_7days_leasing = [By.XPATH, "//div[@class='Dropdown-option'][7]"]
    black_pearl_checkbox = [By.XPATH, "//input[@id='black']"]
    grey_hopelessness_checkbox = [By.XPATH, "//input[@id='grey']"]
    comment_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    submit_order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
    successful_order_modal = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step(f'Ввести имя в поле ввода имени')
    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    @allure.step(f'Ввести фамилию в поле ввода фамилии')
    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    @allure.step(f'Ввести адрес в поле ввода адреса')
    def enter_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    @allure.step(f'Ввести станцию метро в поле ввода станции метро')
    def enter_underground_station(self, underground_station):
        self.driver.find_element(*self.underground_station_input).send_keys(underground_station)

    @allure.step(f'Ввести номер телефона в поле ввода телефона')
    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)

    @allure.step(f'Нажать на кнопку "Далее" под формой заказа самоката')
    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    @allure.step('Нажать на выпадающий список станций метро')
    def click_undergroud_stations_dropdown(self):
        self.driver.find_element(*self.underground_station_input).click()












