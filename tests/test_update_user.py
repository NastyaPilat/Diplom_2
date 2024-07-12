import requests
import pytest
import allure
import endpoints
from request_messages import AUTH_REQUIRED


class TestUpdateUser:

    @allure.title('Изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize("field", ["email", "name"])
    def test_update_user_with_auth(self, field, user):
        register_response = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        login_response = requests.post(
            endpoints.USER_LOGIN_URL, data=user)
        new_value = user[field] + '_'
        user[field] = new_value
        update_response = requests.patch(
            endpoints.USER_URL, data=user, headers={"Authorization": login_response.json()['accessToken']})
        assert update_response.status_code == 200 and update_response.json(
        )['success'] and update_response.json()['user'][field] == new_value

    @allure.title('Изменение данных пользователя без авторизации')
    def test_update_user_without_auth(self, user):
        register_response = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        update_response = requests.patch(endpoints.USER_URL, data=user)
        assert update_response.status_code == 401 and not update_response.json(
        )['success'] and update_response.json()['message'] == AUTH_REQUIRED
