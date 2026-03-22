from random import randint

class Person:
    user_name = 'Сергей'
    email = f'SergeyKulikov42123@ya.ru'
    password = f'SergeyKulikov42123'

class RandomData:
    user_name = 'Случайный'
    email = f'Rand{randint(0,999)}@ya.ru'
    password = f'Rand{randint(1000,9999)}'
    