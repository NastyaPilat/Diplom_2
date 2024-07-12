import requests
import allure
import endpoints
from request_messages import AUTH_REQUIRED


class TestGetUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_user_orders_with_auth(self, user):
        register_response = requests.post(
            endpoints.USER_REGISTER_URL, data=user)
        login_response = requests.post(
            endpoints.USER_LOGIN_URL, data=user)
        response = requests.get(endpoints.ORDERS_URL, headers={
            "Authorization": login_response.json()['accessToken']})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_user_orders_without_auth(self):
        response = requests.get(endpoints.ORDERS_URL)
        assert response.status_code == 401 and not response.json(
        )['success'] and response.json()['message'] == AUTH_REQUIRED
