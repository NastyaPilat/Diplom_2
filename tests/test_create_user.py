import requests
import allure
import endpoints
from request_messages import EMAIL_PASSWORD_NAME_REQUIRED, USER_ALREADY_EXISTS


class TestCreateUser:

    @allure.title('Cоздание уникального пользователя')
    def test_create_unique_user(self, user):
        register_response = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        assert register_response.status_code == 200 and register_response.json()[
            'success']

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, user):
        register_response_1 = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        register_response_2 = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        assert register_response_2.status_code == 403 and not register_response_2.json()['success'] and register_response_2.json()[
            'message'] == USER_ALREADY_EXISTS

    @allure.title('Создание пользователя без обязательного поля')
    def test_create_user_with_missing_field(self, user):
        del user['name']
        register_response = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        assert register_response.status_code == 403 and not register_response.json()['success'] and register_response.json(
        )['message'] == EMAIL_PASSWORD_NAME_REQUIRED
