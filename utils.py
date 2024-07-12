import random
import string
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email():
    return f"test-{generate_random_string(8)}@yandex.ru"


@allure.step('Зарегистрировать пользователя')
def create_new_user():
    return {
        "email": generate_random_email(),
        "password": generate_random_string(8),
        "name": generate_random_string(8)
    }
