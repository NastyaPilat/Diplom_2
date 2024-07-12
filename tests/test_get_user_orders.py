import requests
import allure
import constants
from utils import create_new_user


class TestGetUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_user_orders_with_auth(self):
        user_data = create_new_user()
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user_data)
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user_data)
        response = requests.get(constants.ORDERS_URL, headers={
            "Authorization": login_response.json()['accessToken']})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_user_orders_without_auth(self):
        response = requests.get(constants.ORDERS_URL)
        assert response.status_code == 401 and not response.json(
        )['success'] and response.json()['message'] == "You should be authorised"
