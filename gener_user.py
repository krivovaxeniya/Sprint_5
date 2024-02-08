import random


class GeneratorUser:
    @staticmethod
    def generate_user():
        name = 'Ксения'
        login = f'krivova_5{random.randint(100, 999)}@ya.ru'
        password = random.randint(100000, 999999)
        user_data = [name, login, password]
        return user_data
