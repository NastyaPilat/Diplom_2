import pytest
import requests
import constants
from utils import create_new_user


@pytest.fixture(scope="class")
def example_ingredients():
    response = requests.get(constants.INGREDIENTS_URL).json()['data']
    return [ingredient['_id'] for ingredient in response[:2]]


@pytest.fixture
def user():
    return create_new_user()
