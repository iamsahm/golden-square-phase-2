import pytest
from lib.customer import *
from unittest.mock import Mock
from unittest import mock
import json
jsonmenu = open('tests/menu.json')
formatted_menu = json.load(jsonmenu)
import datetime
import twilio

def test_order_appends_order():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = formatted_menu

    customer = Customer(requester_mock)
    customer.order_dish('Original Blend Burger - 8 Pack')
    customer.order_dish('Mooby\'s Meal Kit - 6 Pack')
    customer.order_dish('Goldbelly "Burger Bash" Pack')
    assert customer.order_list == ['Original Blend Burger - 8 Pack', 'Mooby\'s Meal Kit - 6 Pack', 'Goldbelly "Burger Bash" Pack']

def test_ordering_non_menu_item_raises_exception():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = formatted_menu
    customer = Customer(requester_mock)
    with pytest.raises(Exception) as e:
        customer.order_dish('big nice things')
    assert str(e.value) == 'That\'s not on the menu! Choose something else.'


def test_return_receipt_returns_receipt_w_total():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = formatted_menu
    customer = Customer(requester_mock)
    customer.order_dish('Original Blend Burger - 8 Pack')
    customer.order_dish('Mooby\'s Meal Kit - 6 Pack')
    customer.order_dish('Goldbelly "Burger Bash" Pack')
    assert customer.return_receipt() == f'Here\'s your receipt:\nOriginal Blend Burger - 8 Pack £31.9\nMooby\'s Meal Kit - 6 Pack £79\nGoldbelly "Burger Bash" Pack £109\n\nTotal: £{31.9+79+109}'
    # Customer
    # add a load of orders
    # customer.orderlist returns string receipt with total

# # Use the twilio-python package to implement this next one. You will need to use mocks too.
def test_twilio_returns_string_with_time():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = formatted_menu
    customer = Customer(requester_mock)
    customer.order_dish('Original Blend Burger - 8 Pack')
    delivery_time = datetime.datetime.now()+ datetime.timedelta(minutes = 30)
    assert customer.order_confirmation() == f"Sent from your Twilio trial account - Thank you! Your order was placed and will be delivered before {delivery_time.strftime('%H:%M')}"



# As a customer
# So that I am reassured that my order will be delivered on time
# I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

# Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?

