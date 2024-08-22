import config
from pages.main_page import QuestionsPage
from faker import Faker
fake = Faker('ru_RU')
questions_and_answers = [
    (QuestionsPage.question_cost_and_payment_ways, QuestionsPage.answer_cost_and_payment_ways, config.FIRST_QUESTION_ANSWER),
    (QuestionsPage.question_multiple_scooters, QuestionsPage.answer_multiple_scooters, config.SECOND_QUESTION_ANSWER),
    (QuestionsPage.question_leasing_time, QuestionsPage.answer_leasing_time, config.THIRD_QUESTION_ANSWER),
    (QuestionsPage.question_is_possible_to_order_today, QuestionsPage.answer_is_possible_to_deliver_today, config.FOURTH_QUESTION_ANSWER),
    (QuestionsPage.question_is_possible_to_extend_leasing, QuestionsPage.answer_is_possible_to_extend_leasing, config.FIFTH_QUESTION_ANSWER),
    (QuestionsPage.question_charger, QuestionsPage.answer_charger, config.SIXTH_QUESTION_ANSWER),
    (QuestionsPage.question_is_possible_to_cancel_order, QuestionsPage.answer_is_possible_to_cancel_order, config.SEVENTH_QUESTION_ANSWER),
    (QuestionsPage.question_is_possible_to_deliver_off_mkad, QuestionsPage.answer_is_possible_to_deliver_off_mkad, config.EIGHTH_QUESTION_ANSWER),
]



order_data = [
    {
        "name": fake.name()[:5],
        "last_name": fake.last_name()[:10],
        "address": fake.address()[:10],
        "underground_station": "Печатники",
        "phone_number": '89037876473',
        "delivery_date": '12.08.2025',
        'comment': 'привет'
    },
    {
        "name": fake.name()[:5],
        "last_name": fake.last_name()[:10],
        "address": fake.address()[:10],
        "underground_station": "Печатники",
        "phone_number": '89037876474',
        "delivery_date": '15.08.2025',
        'comment': 'здравствуйте'
    }
]

