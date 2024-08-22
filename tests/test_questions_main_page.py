import time
import pytest
from selenium import webdriver
import config
import data
from pages.main_page import QuestionsPage
import allure
from conftest import driver


class TestQuestionsMainPage:

    @allure.title('Проверяем тексты ответов на вопросы в аккордеоне')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', data.questions_and_answers)
    def test_first_answer_has_a_correct_text(self, driver, question_locator, answer_locator, expected_answer):
        main_page = QuestionsPage(driver)
        main_page.open_page(config.BASE_URL)
        main_page.wait_and_find_element(question_locator)
        main_page.scroll_to_questions_accordion()
        main_page.click_element(question_locator)
        answer_text = main_page.wait_and_find_element(answer_locator).text
        assert answer_text == expected_answer












