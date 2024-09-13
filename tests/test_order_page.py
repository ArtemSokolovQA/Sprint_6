import pytest
import config
import data
from pages.main_page import QuestionsPage
from pages.order_scooter_page import OrderScooterPage
import allure
from faker import Faker
from conftest import driver


class TestOrderScooterPage:
    fake = Faker('ru_RU')

    @allure.title('Проверка возможности перехода к странице оформления заказа по клику на кнопку "заказать" в хедере главной страницы')
    def test_navigation_from_main_page_to_order_page_with_header_order_button(self, driver):
        main_page = QuestionsPage(driver)
        main_page.open_page(config.BASE_URL)
        main_page.click_order_scooter_button()
        current_url = driver.current_url
        assert current_url == config.ORDER_SCOOTER_PAGE_URL

    @allure.title('Проверка возможности перехода к странице оформления заказа по клику на кнопку "заказать" в середине главной страницы')
    def test_navigation_from_main_page_to_order_page_with_middle_order_button(self, driver):
        main_page = QuestionsPage(driver)
        main_page.open_page(config.BASE_URL)
        main_page.scroll_to_middle_order_button()
        main_page.click_middle_order_scooter_button()
        current_url = main_page.get_current_url()
        assert current_url == config.ORDER_SCOOTER_PAGE_URL

    @pytest.mark.parametrize('order_data', data.order_data)
    def test_order_scooter_positive_flow(self, driver, order_data):
        order_page = OrderScooterPage(driver)
        order_page.open_page(config.ORDER_SCOOTER_PAGE_URL)
        order_page.set_name(order_data['name'])
        order_page.set_last_name(order_data['last_name'])
        order_page.set_address(order_data['address'])
        order_page.set_underground_station(order_data['underground_station'])
        order_page.click_underground_station_element()
        order_page.set_phone_number(order_data['phone_number'])
        order_page.click_continue_button()
        order_page.set_delivery_date(order_data['delivery_date'])
        order_page.click_about_leasing_title()
        order_page.click_leasing_period_dropdown()
        order_page.click_dropdown_leasing_element()
        order_page.click_checkbox_scooter_colour_grey()
        order_page.click_order_button_about_leasing()
        order_page.click_submit_order_button()
        successful_order_title = order_page.check_successful_order_title()
        assert successful_order_title











