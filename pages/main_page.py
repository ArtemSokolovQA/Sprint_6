import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QuestionsPage(BasePage):

    #  локаторы кнопок вопросов в аккордеоне
    question_cost_and_payment_ways = (By.XPATH, "//div[@id='accordion__heading-0']")
    question_multiple_scooters = (By.XPATH, "//div[@id='accordion__heading-1']")
    question_leasing_time = (By.XPATH, "//div[@id='accordion__heading-2']")
    question_is_possible_to_order_today = (By.XPATH, "//div[@id='accordion__heading-3']")
    question_is_possible_to_extend_leasing = (By.XPATH, "//div[@id='accordion__heading-4']")
    question_charger = (By.XPATH, "//div[@id='accordion__heading-5']")
    question_is_possible_to_cancel_order = (By.XPATH, "//div[@id='accordion__heading-6']")
    question_is_possible_to_deliver_off_mkad = (By.XPATH, "//div[@id='accordion__heading-7']")

    #  локаторы ответов на вопросы аккордеона
    answer_cost_and_payment_ways = (By.XPATH, "//div[@id='accordion__panel-0']")
    answer_multiple_scooters = (By.XPATH, "//div[@id='accordion__panel-1']")
    answer_leasing_time = (By.XPATH, "//div[@id='accordion__panel-2']")
    answer_is_possible_to_deliver_today = (By.XPATH, "//div[@id='accordion__panel-3']")
    answer_is_possible_to_extend_leasing = (By.XPATH, "//div[@id='accordion__panel-4']")
    answer_charger = (By.XPATH, "//div[@id='accordion__panel-5']")
    answer_is_possible_to_cancel_order = (By.XPATH, "//div[@id='accordion__panel-6']")
    answer_is_possible_to_deliver_off_mkad = (By.XPATH, "//div[@id='accordion__panel-7']")

    order_scooter_button_header = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    order_scooter_button_middle = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Кликнуть по кнопке "заказать" в хедере страницы')
    def click_order_scooter_button(self):
        order_scooter_button = self.wait_and_find_element(self.order_scooter_button_header)
        order_scooter_button.click()

    @allure.step('Скроллить страницу до кнопки "заказать" в центре главной страницы')
    def scroll_to_middle_order_button(self):
        middle_order_button = self.wait_and_find_element(self.order_scooter_button_middle)
        self.scroll_to_element(middle_order_button)

    @allure.step('Кликнуть по кнопке "заказать" в центре главной страницы')
    def click_middle_order_scooter_button(self):
        middle_order_scooter_button = self.wait_and_find_element(self.order_scooter_button_middle)
        middle_order_scooter_button.click()


    @allure.step('Скроллить до аккорденона с вопросами')
    def scroll_to_questions_accordion(self):
        questions_accordion = self.wait_and_find_element(self.question_is_possible_to_extend_leasing)
        self.scroll_to_element(questions_accordion)



















