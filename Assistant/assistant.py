import os
from random import randint

students = {1: 'Аузін Роман Олександрович',
            2: 'Бабченко Роман Олексійович',
            3: 'Бессчастний Сергій Володимирович',
            4: 'Грецький Ігор Олександрович',
            5: 'Депешко Владислав Олександрович',
            6: 'Каланча Інга Георгіївна',
            7: 'Мармиш Костянтин Михайлович',
            8: 'Мовчан Ігор Ігорович',
            9: 'Поддубіцький Дмитро Анатолійович',
            10: 'Свірін Сергій Вадимович',
            11: 'Стегніщева Олександра Миколаївна',
            12: 'Столітній Антон Володимирович',
            13: 'Холодний Юрій Андрійович',
            14: 'Цагурія Лука Бадрієвич',
            15: 'Шубський Данил Євгенович'}


def speaker(text, punctuation=''):
    os.system("say " + text)
    print(text)


def hello():
    speaker('Привет ребятки!')
    speaker('Как там успехи в питоне?')


def what_do_yo_want():
    speaker('Что вам нужно от меня?')


def random_student():
    speaker('Так, ну давайте подумаем кого отправить к доске...')
    while True:
        student = students[randint(1, 15)]
        speaker('К доске пойдет {}'.format(student))
        speaker('Присутствует?')
        answer = input().lower()
        if answer == 'да':
            speaker('Отлично')
            break
        elif answer == 'нет':
            speaker('Давайте выберем другого студента')
            continue
        else:
            speaker('Я не понимаю чего вы от меня хотите!')
            speaker('Решайте сами')
            break


def run():
    hello()
    while True:
        command = (input('Выбрать кто пойдет к доске?\n')).lower()
        if command == 'да':
            random_student()
        elif command == 'нет':
            speaker('Нет так нет!')
        else:
            speaker('Я не понимаю чего вы от меня хотите!')
