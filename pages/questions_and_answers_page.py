import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class QuestionsPage(BasePage):

    #  локаторы кнопок вопросов в аккордеоне
    question_cost_and_payment_ways = [By.XPATH, "//div[@id='accordion__heading-0']"]
    question_multiple_scooters = [By.XPATH, "//div[@id='accordion__heading-1']"]
    question_leasing_time = [By.XPATH, "//div[@id='accordion__heading-2']"]
    question_is_possible_to_order_today = [By.XPATH, "//div[@id='accordion__heading-3']"]
    question_is_possible_to_extend_leasing = [By.XPATH, "//div[@id='accordion__heading-4']"]
    question_charger = [By.XPATH, "//div[@id='accordion__heading-5']"]
    question_is_possible_to_cancel_order = [By.XPATH, "//div[@id='accordion__heading-6']"]
    question_is_possible_to_deliver_off_mkad = [By.XPATH, "//div[@id='accordion__heading-7']"]

    #  локаторы ответов на вопросы аккордеона
    answer_cost_and_payment_ways = [By.XPATH, "//div[@id='accordion__panel-0']"]
    answer_multiple_scooters = [By.XPATH, "//div[@id='accordion__panel-1']"]
    answer_leasing_time = [By.XPATH, "//div[@id='accordion__panel-2']"]
    answer_is_possible_to_deliver_today = [By.XPATH, "//div[@id='accordion__panel-3']"]
    answer_is_possible_to_extend_leasing = [By.XPATH, "//div[@id='accordion__panel-4']"]
    answer_charger = [By.XPATH, "//div[@id='accordion__panel-5']"]
    answer_is_possible_to_cancel_order = [By.XPATH, "//div[@id='accordion__panel-6']"]
    answer_is_possible_to_deliver_off_mkad = [By.XPATH, "//div[@id='accordion__panel-7']"]

    order_scooter_button_header = [By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    order_scooter_button_middle = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"]

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Кликнуть по кнопке первого вопроса в аккордеоне')
    def click_first_question_button(self):
        first_question_button = self.wait_and_find_element(self.question_cost_and_payment_ways)
        first_question_button.click()

    @allure.step('Кликнуть по кнопке второго вопроса в аккордеоне')
    def click_second_question_button(self):
        second_question_button = self.wait_and_find_element(self.question_multiple_scooters)
        second_question_button.click()

    @allure.step('Кликнуть по кнопке третьего вопроса в аккордеоне')
    def click_third_question_button(self):
        third_question_button = self.wait_and_find_element(self.question_leasing_time)
        third_question_button.click()

    @allure.step('Кликнуть по кнопке четвертого вопроса в аккордеоне')
    def click_fourth_question_button(self):
        fourth_question_button = self.wait_and_find_element(self.question_is_possible_to_order_today)
        fourth_question_button.click()

    @allure.step('Кликнуть по кнопке  пятого в аккордеоне')
    def click_fifth_question_button(self):
        fifth_question_button = self.wait_and_find_element(self.question_is_possible_to_extend_leasing)
        fifth_question_button.click()

    @allure.step('Кликнуть по кнопке шестого вопроса в аккордеоне')
    def click_sixth_question_button(self):
        sixth_question_button = self.wait_and_find_element(self.question_charger)
        sixth_question_button.click()

    @allure.step('Кликнуть по кнопке седьмого вопроса в аккордеоне')
    def click_seventh_question_button(self):
        seventh_question_button = self.wait_and_find_element(self.question_is_possible_to_cancel_order)
        seventh_question_button.click()

    @allure.step('Кликнуть по кнопке восьмого вопроса в аккордеоне')
    def click_eighth_question_button(self):
        eighth_question_button = self.wait_and_find_element(self.question_is_possible_to_deliver_off_mkad)
        eighth_question_button.click()

    @allure.step('Получить ответ на первый вопрос')
    def get_answer_first_question(self):
        first_answer_text = self.wait_and_find_element(self.answer_cost_and_payment_ways).text
        return first_answer_text

    @allure.step('Получить ответ на второй вопрос')
    def get_answer_second_question(self):
        second_answer_text = self.wait_and_find_element(self.answer_multiple_scooters).text
        return second_answer_text

    @allure.step('Получить ответ на третий вопрос')
    def get_answer_third_question(self):
        third_answer_text = self.wait_and_find_element(self.answer_leasing_time).text
        return third_answer_text

    @allure.step('Получить ответ на четвертый вопрос')
    def get_answer_fourth_question(self):
        fourth_answer_text = self.wait_and_find_element(self.answer_is_possible_to_deliver_today).text
        return fourth_answer_text

    @allure.step('Получить ответ на пятый вопрос')
    def get_answer_fifth_question(self):
        fifth_answer_text = self.wait_and_find_element(self.answer_is_possible_to_extend_leasing).text
        return fifth_answer_text

    @allure.step('Получить ответ на шестой вопрос')
    def get_answer_sixth_question(self):
        sixth_answer_text = self.wait_and_find_element(self.answer_charger).text
        return sixth_answer_text

    @allure.step('Получить ответ на седьмой вопрос')
    def get_answer_seventh_question(self):
        seventh_answer_text = self.wait_and_find_element(self.answer_is_possible_to_cancel_order).text
        return seventh_answer_text

    @allure.step('Получить ответ на восьмой вопрос')
    def get_answer_eighth_question(self):
        eighth_answer_text = self.wait_and_find_element(self.answer_is_possible_to_deliver_off_mkad).text
        return eighth_answer_text

    @allure.step('Кликнуть по кнопке "заказать" в хедере страницы')
    def click_order_scooter_button(self):
        order_scooter_button = self.wait_and_find_element(self.order_scooter_button_header)
        order_scooter_button.click()

    @allure.step('Скроллить страницу до кнопки "заказать" в центре главной страницы')
    def scroll_to_middle_order_button(self):
        self.wait_and_find_element(self.order_scooter_button_middle)
        self.scroll_to_element(self.order_scooter_button_middle)

    @allure.step('Кликнуть по кнопке "заказать" в центре главной страницы')
    def click_middle_order_scooter_button(self):
        middle_order_scooter_button = self.wait_and_find_element(self.order_scooter_button_middle)
        middle_order_scooter_button.click()




















