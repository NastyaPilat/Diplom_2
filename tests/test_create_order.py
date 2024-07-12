import requests
import allure
import constants
from request_messages import INGREDIENT_IDS_REQUIRED


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, example_ingredients, user):
        register_response = requests.post(
            constants.USER_REGISTER_URL, data=user)
        login_response = requests.post(
            constants.USER_LOGIN_URL, data=user)
        data = {'ingredients': example_ingredients}
        response = requests.post(constants.ORDERS_URL, data=data, headers={
            "Authorization": login_response.json()['accessToken']})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Создание заказа без авторизацией')
    def test_create_order_without_auth(self, example_ingredients):
        data = {'ingredients': example_ingredients}
        response = requests.post(constants.ORDERS_URL, data=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        data = {'ingredients': []}
        response = requests.post(constants.ORDERS_URL, data=data)
        assert response.status_code == 400 and not response.json(
        )['success'] and response.json()['message'] == INGREDIENT_IDS_REQUIRED

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients_hash(self, example_ingredients):
        data = {'ingredients': example_ingredients}
        data['ingredients'][0] = ''
        response = requests.post(constants.ORDERS_URL, data=data)
        assert response.status_code == 500
