import random
from faker import Faker
import allure
import requests
from data import Url

fake = Faker('ru_RU')

def email():
    generated_email = fake.email()
    return generated_email

def username():
    generated_username = fake.user_name()
    return generated_username

def password():
    generated_password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return generated_password

@allure.step('Метод для генерации данных пользователя')
def payload_create_user():
    """Метод для генерации данных пользователя"""
    payload = {
        'email': email(),
        'password': password(),
        'name': username()
    }
    return payload

@allure.step('Метод для генерации данных заказа')
def payload_order():
    response_ingr = requests.get(Url.GET_INGREDIENTS)
    data = response_ingr.json()
    bun_list = []
    sauce_list = []
    main_list = []
    burger_list = []
    for i in range(len(data['data'])):
        if data['data'][i]['type'] == "bun":
            bun_list.append(data['data'][i]['_id'])
        if data['data'][i]['type'] == "main":
            main_list.append(data['data'][i]['_id'])
        if data['data'][i]['type'] == "sauce":
            sauce_list.append(data['data'][i]['_id'])

    burger_list.append(bun_list[random.randint(0,len(bun_list)-1)])
    choise_sauce = random.randint(0,len(sauce_list))
    if choise_sauce != len(sauce_list):
        for i in range(len(sauce_list)):
            burger_list.append(sauce_list[i])

    choise_main = random.randint(0,len(main_list))
    if choise_main != len(main_list):
        for i in range(len(main_list)):
            burger_list.append(main_list[i])

    return {
         'ingredients': burger_list
    }
