import pytest
import requests
import constants


@pytest.fixture(scope="class")
def example_ingredients():
    response = requests.get(constants.INGREDIENTS_URL).json()['data']
    return [ingredient['_id'] for ingredient in response[:2]]
