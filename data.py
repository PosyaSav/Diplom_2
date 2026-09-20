class Url:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    CREATE_USER = BASE_URL + 'api/auth/register'        #   POST    Создание пользователя
    LOGIN_USER = BASE_URL + 'api/auth/login'            #   POST    Авторизация 
    DELETE_USER = BASE_URL + 'api/auth/user'            #   DELETE  Удаление пользователя
    CREATE_ORDER = BASE_URL + 'api/orders'              #   POST    Создание заказа
    GET_INGREDIENTS = BASE_URL + 'api/ingredients'      #   GET     Получение ингредиентов

class ResponseMessage:
    USER_EXISTS = 'User already exists'
    EMPTY_FIELD = 'Email, password and name are required fields'
    INCORRECT = 'email or password are incorrect'
    EMPTY_IDS = 'Ingredient ids must be provided'
