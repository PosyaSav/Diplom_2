import allure
import pytest
import requests
from data import ResponseMessage, Url

class TestLoginUser:

    @allure.title('Тест успешной авторизации пользователя')
    def test_successful_login_user(self, create_user):
        payload_login = create_user['payload']
        response_login = requests.post(Url.LOGIN_USER, data=payload_login)

        assert 200 == response_login.status_code
        assert response_login.json()['success']

    @allure.title('Тест авторизации пользователя с невернымы логином или паролем')
    @pytest.mark.parametrize('bad',['email', 'password'])
    def test_login_user_bad_auth(self, create_user, bad):
        payload_login = create_user['payload']
        payload_login[bad] += '1'
        response_login = requests.post(Url.LOGIN_USER, data=payload_login)

        assert 401 == response_login.status_code
        assert response_login.json()['message'] == ResponseMessage.INCORRECT  
