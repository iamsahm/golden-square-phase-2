Here is a project to test your golden square skills overall:

class Customer():
    init:
        order list

    see_menu()
        returns menu list

    order_dish(dish)
        

    return_receipt

class Menu()
    init:
        dictionary of menu items: price





As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

test_see_menu_returns_list():
    call Menu object inside Customer and assert return shows string of menu items

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.
test_order_appends_order():
    call Customer
    customer.order adds items to order list

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.
test_return_receipt_returns_receipt_w_total():
    Customer
    add a load of orders
    customer.orderlist returns string receipt with total

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?

