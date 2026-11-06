import allure
import requests
from data import Url
import helpers

class TestCreateOrder:

    @allure.title('Тест создания заказа с авторизацией пользователя')
    def test_create_order_with_auth(self, create_user):
        user_data = create_user
        headers = {"Authorization":user_data['token']}
        payload_create_order = helpers.payload_order()
        response_create_order = requests.post(Url.CREATE_ORDER, data=payload_create_order, headers=headers)

        assert 200 == response_create_order.status_code
        assert response_create_order.json()['success']
        assert user_data['payload']['name'] == response_create_order.json()['order']['owner']['name']

    @allure.title('Тест создания заказа без авторизации пользователя')
    def test_create_order_without_auth(self):
        payload_create_order = helpers.payload_order()
        response_create_order = requests.post(Url.CREATE_ORDER, data=payload_create_order)

        assert 200 == response_create_order.status_code
        assert response_create_order.json()['success']
        assert response_create_order.json().get('owner') is None

    @allure.title('Тест создания заказа с ингредиентами')
    def test_create_order_with_ingr(self):
        payload_create_order = helpers.payload_order()
        response_create_order = requests.post(Url.CREATE_ORDER, data=payload_create_order)

        assert 200 == response_create_order.status_code
        assert response_create_order.json()['success']
        assert response_create_order.json()['order'].get('number') is not None

    @allure.title('Тест создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_bad_hash_ingr(self):
        payload_create_order = {'ingredients': ['61c0c5a71d1f82001bdaaa7']}
        response_create_order = requests.post(Url.CREATE_ORDER, data=payload_create_order)

        assert 500 == response_create_order.status_code

    @allure.title('Тест создания заказа без ингредиентов')
    def test_create_order_without_ingr(self):
        response_create_order = requests.post(Url.CREATE_ORDER, data={'ingredients': ""})

        assert 400 == response_create_order.status_code
        assert not response_create_order.json()['success']
