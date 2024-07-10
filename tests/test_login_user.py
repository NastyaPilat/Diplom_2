import requests
import constants
from utils import create_new_user
import allure


class TestLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user_data)
        assert login_response.status_code == 200 and login_response.json()[
            'success']

    @allure.title('Логин с неверным логином и паролем')
    def test_login_with_invalid_credentials(self):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        user_data['password'] = ''
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user_data)
        assert login_response.status_code == 401 and not login_response.json(
        )['success'] and login_response.json()['message'] == "email or password are incorrect"
