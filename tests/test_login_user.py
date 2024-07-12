import requests
import allure
import constants
from request_messages import INVALID_CREDENTIALS


class TestLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self, user):
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user)
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user)
        assert login_response.status_code == 200 and login_response.json()[
            'success']

    @allure.title('Логин с неверным логином и паролем')
    def test_login_with_invalid_credentials(self, user):
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user)
        user['password'] = ''
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user)
        assert login_response.status_code == 401 and not login_response.json(
        )['success'] and login_response.json()['message'] == INVALID_CREDENTIALS
