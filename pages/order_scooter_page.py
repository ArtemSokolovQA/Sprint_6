import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import data
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    #  Первая форма заказа самоката
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    underground_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    uderground_station_dropdown = (By.XPATH, "//div[@class='select-search__select']")
    underground_station_element = (By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='Печатники']")
    phone_number_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    continue_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    #  Вторая форма заказа самоката
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    leasing_period_dropdown = (By.XPATH, "//div[@class='Dropdown-control']")
    dropdown_1day_leasing = (By.XPATH, "//div[@class='Dropdown-option'][1]")
    dropdown_2days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][2]")
    dropdown_3days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][3]")
    dropdown_4days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][4]")
    dropdown_5days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][5]")
    dropdown_6days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][6]")
    dropdown_7days_leasing = (By.XPATH, "//div[@class='Dropdown-option'][7]")
    black_pearl_checkbox = (By.XPATH, "//input[@id='black']")
    grey_hopelessness_checkbox = (By.XPATH, "//input[@id='grey']")
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    submit_order_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    successful_order_modal = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step(f'Ввести имя в поле ввода имени')
    def set_name(self, name):
        self.set_input(self.name_input, name)

    @allure.step(f'Ввести фамилию в поле ввода фамилии')
    def set_last_name(self, last_name):
        self.set_input(self.last_name_input, last_name)

    @allure.step(f'Ввести адрес в поле ввода адреса')
    def set_address(self, address):
        self.set_input(self.address_input, address)

    @allure.step(f'Ввести станцию метро в поле ввода станции метро')
    def set_underground_station(self, underground_station):
        self.set_input(self.underground_station_input, underground_station)

    @allure.step(f'Ввести номер телефона в поле ввода телефона')
    def set_phone_number(self, phone_number):
        self.set_input(self.phone_number_input, phone_number)

    @allure.step(f'Нажать на кнопку "Далее" под формой заказа самоката')
    def click_continue_button(self):
        self.click_element(self.continue_button)

    @allure.step('Нажать на выпадающий список станций метро')
    def click_underground_stations_dropdown(self):
        self.click_element(self.uderground_station_dropdown)

    @allure.step('Нажать на введенную станцию в дропдауне')
    def click_underground_station_element(self):
        self.click_element(self.underground_station_element)













