import requests
from lib.customer import *
from unittest.mock import Mock


def test_see_menu_returns_list():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = [{
        "id": "vegan-burger-patties-12-pack",
        "img": "https://goldbelly.imgix.net/uploads/showcase_media_asset/image/119472/vegan-burger-patties-12-pack.56f31f18b126e7f84b02b6f1babd5d12.jpg?ixlib=react-9.0.2&auto=format&ar=1%3A1",
        "name": "Burgerlords",
        "dsc": "Vegan Burger Patties - 12 Pack",
        "price": 79,
        "rate": 4,
        "country": "Los Angeles, CA"
        }]
    
    customer = Customer(requester_mock)
    result = customer.see_menu()
    assert result == 'Today\'s menu:\n Vegan Burger Patties - 12 Pack, £79\n'