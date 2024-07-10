import random
import string
import allure


@allure.step('Зарегистрировать пользователя')
def create_new_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_email():
        return f"test-{generate_random_string(10)}@yandex.ru"

    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    return user_data
