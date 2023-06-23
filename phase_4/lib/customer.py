import requests
import json
import pytest
import os
from twilio.rest import Client
import twilio
import datetime

class Customer:
    def __init__(self, requester):
        self.order_list = []
        self._requester = requester
        jsonResponse = self._requester.get('https://free-food-menus-api-production.up.railway.app/burgers').json()
        self.menu = {}
        for i in jsonResponse:
            key = i['dsc']
            value = i['price']
            self.menu[key] = value

    def see_menu(self):
        menu_string = ''
        for i in self.menu.items():
            menu_string +=i[0]+', £' + str(i[1])+'\n'
        print (self.menu)
        return f'Today\'s menu:\n {menu_string}'

    def order_dish(self, order):
        if order not in self.menu.keys():
            raise Exception('That\'s not on the menu! Choose something else.')

        self.order_list.append(order)

    def return_receipt(self):
        order = []
        total = 0 
        for i in self.order_list:
            total += self.menu[i]
            order.append(f'{i} £{self.menu[i]}')
        order_string = '\n'.join(order)
        return f'Here\'s your receipt:\n{order_string}\n\nTotal: £{total}'
    
    def order_confirmation(self):
            
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        delivery_time = datetime.datetime.now()+ datetime.timedelta(minutes = 30)

        message = client.messages \
            .create(
                body=f"Thank you! Your order was placed and will be delivered before {delivery_time.strftime('%H:%M')}",
                from_=os.environ['TWILIO_MOBILE_NUMBER'],
                to=os.environ['MY_MOBILE']
            )

        return(message.body)

