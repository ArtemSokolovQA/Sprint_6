import time
import pytest
from selenium import webdriver
import config
import data
from pages.questions_and_answers_page import QuestionsPage
import allure


class TestQuestionsMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(config.BASE_URL)

    @allure.title('Проверяем тексты ответов на вопросы в аккордеоне')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', data.questions_and_answers)
    def test_first_answer_has_a_correct_text(self, question_locator, answer_locator, expected_answer):
        main_page = QuestionsPage(self.driver)
        question_element = self.driver.find_element(*question_locator)
        main_page.scroll_to_element(question_element)
        main_page.wait_questions_page_loaded()
        question_element.click()
        answer_text = self.driver.find_element(*answer_locator).text
        assert answer_text == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()











