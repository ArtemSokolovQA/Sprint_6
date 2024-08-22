import time
from selenium.webdriver.support.ui import Select
import faker.providers.date_time
import pytest
from selenium import webdriver
import config
import data
from pages.questions_and_answers_page import QuestionsPage
from pages.order_scooter_page import OrderScooterPage
import allure
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestOrderScooterPage:
    driver = None
    fake = Faker('ru_RU')

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Проверка возможности перехода к странице оформления заказа по клику на кнопку "заказать" в хедере главной страницы')
    def test_navigation_from_main_page_to_order_page_with_header_order_button(self):
        self.driver.get(config.BASE_URL)
        main_page = QuestionsPage(self.driver)
        main_page.click_order_scooter_button()
        current_url = self.driver.current_url
        assert current_url == config.ORDER_SCOOTER_PAGE_URL

    @allure.title('Проверка возможности перехода к странице оформления заказа по клику на кнопку "заказать" в середине главной страницы')
    def test_navigation_from_main_page_to_order_page_with_middle_order_button(self):
        self.driver.get(config.BASE_URL)
        main_page = QuestionsPage(self.driver)
        main_page.scroll_to_middle_order_button()
        main_page.click_middle_order_scooter_button()
        current_url = self.driver.current_url
        assert current_url == config.ORDER_SCOOTER_PAGE_URL

    # @pytest.mark.parametrize('order_data', data.order_data)
    # def test_order_scooter_positive_flow(self, order_data):
    #     self.driver.get(config.ORDER_SCOOTER_PAGE_URL)
    #     order_page = OrderScooterPage(self.driver)
    #     order_page.enter_name(order_data['name'])
    #     order_page.enter_last_name(order_data['last_name'])
    #     order_page.enter_address(order_data['address'])
    #     order_page.enter_underground_station(order_data['underground_station'])
    #     self.driver.find_element(By.XPATH,
    #                              f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='{order_data['underground_station']}']").click()
    #     order_page.enter_phone_number(order_data['phone_number'])
    #     order_page.click_continue_button()











