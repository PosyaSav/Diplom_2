import pytest
import requests
from data import Url
import helpers

@pytest.fixture
def create_user():
    payload_create = helpers.payload_create_user()
    response_create = requests.post(Url.CREATE_USER, data=payload_create)
    yield {
        'payload': payload_create,
        'token': response_create.json()['accessToken']
    }
    headers = {"Authorization":response_create.json()['accessToken']}
    requests.delete(Url.DELETE_USER, headers=headers)
