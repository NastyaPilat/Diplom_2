import requests
import constants
from utils import create_new_user
import pytest
import allure


class TestUpdateUser:

    @pytest.mark.parametrize("field", ["email", "name"])
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_update_user_with_auth(self, field):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user_data)
        new_value = create_new_user()[field]
        user_data[field] = new_value
        update_response = requests.patch(
            constants.USER_URL, data=user_data, headers={"Authorization": login_response.json()['accessToken']})
        assert update_response.status_code == 200 and update_response.json(
        )['success'] and update_response.json()['user'][field] == new_value

    @allure.title('Изменение данных пользователя без авторизации')
    def test_update_user_without_auth(self):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        update_response = requests.patch(constants.USER_URL, data=user_data)
        assert update_response.status_code == 401 and not update_response.json(
        )['success'] and update_response.json()['message'] == "You should be authorised"
