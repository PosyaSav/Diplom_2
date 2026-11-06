import allure
import pytest
import requests
from data import ResponseMessage, Url
import helpers

class TestCreateUser:

    @allure.title('Тест успешного создания пользователя')
    def test_successful_create_user(self):
        payload_create = helpers.payload_create_user()
        response_create = requests.post(Url.CREATE_USER, data=payload_create)
        headers = {"Authorization":response_create.json()['accessToken']}
        requests.delete(Url.DELETE_USER, headers=headers)    

        assert 200 == response_create.status_code
        assert response_create.json()['success']

    @allure.title('Тест создания существующего пользователя')
    def test_create_same_user(self, create_user):
        payload_create = create_user['payload']
        response_create = requests.post(Url.CREATE_USER, data=payload_create)

        assert 403 == response_create.status_code
        assert response_create.json()['message'] == ResponseMessage.USER_EXISTS

    @allure.title('Тест создания пользователя с одним пустым обязательным полем')
    @pytest.mark.parametrize('empty',['email', 'password', 'name'])
    def test_create_user_one_empty_field(self, empty):
        payload_create = helpers.payload_create_user()
        del payload_create[empty]
        response_create = requests.post(Url.CREATE_USER, data=payload_create)

        assert 403 == response_create.status_code
        assert response_create.json()['message'] == ResponseMessage.EMPTY_FIELD
