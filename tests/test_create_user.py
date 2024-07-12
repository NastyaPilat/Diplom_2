import requests
import allure
import constants
from utils import create_new_user


class TestCreateUser:

    @allure.title('Cоздание уникального пользователя')
    def test_create_unique_user(self):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        assert register_response.status_code == 200 and register_response.json()[
            'success']

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self):
        user_data = create_new_user()
        register_response_1 = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        register_response_2 = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        assert register_response_2.status_code == 403 and not register_response_2.json()['success'] and register_response_2.json()[
            'message'] == "User already exists"

    @allure.title('Создание пользователя без обязательного поля')
    def test_create_user_with_missing_field(self):
        user_data = create_new_user()
        del user_data['name']
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        assert register_response.status_code == 403 and not register_response.json()['success'] and register_response.json(
        )['message'] == "Email, password and name are required fields"
