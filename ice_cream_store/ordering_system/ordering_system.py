"""ice cream ORDERING SYSTEM for below zero company

    Goal: Improve customer service by streamlining the ordering process

    Requirements:
    Staff at station: Price is calculated and customer pays
    Staff at counter: Order is forwarded to them, they complete the order and give it to the customer

"""

from random import *

"""*****************PRICES OF INDIVIDUAL ITEMS*******************************"""

# dictionary to store the cone type prices
cone_type_dict = {'Plain Cone': 1.5, 'Waffle Cone': 2, 'Cup': 1}
cone_type_dict1 = {1: 'Plain Cone', 2: 'Waffle Cone', 3: 'Cup'}

# dictionary to store the scope flavour prices
scope_flavours_dict = {1: 'Vanilla', 2: 'Strawberry', 3: 'Chocolate', 4: 'Caramel',
                       5: 'Mint', 6: 'Rainbow', 7: 'Coffee', 8: 'Bubble Gum'}

# dictionary to store the topping choices prices
topping_choices_dict = {'Peanuts': 0.75, 'Caramel Sauce': 0.5, 'Rainbow Sprinkles': 0.5,
                        'Pecan': 1, 'Chocolate Sprinkles': 0.5}

topping_choices_dict1 = {1: 'Peanuts', 2: 'Caramel Sauce', 3: 'Rainbow Sprinkles',
                         4: 'Pecan', 5: 'Chocolate Sprinkles'}


# functions to display to the user the prices and allow them to choose
def print_cone_type():
    cone_type_list = [[1, 'Plain Cone', 1.5],
                      [2, 'Waffle Cone', 2],
                      [3, 'Cup', 1]]

    print(": Item  : Name           : Price :")
    for cone in cone_type_list:
        print(":", cone[0], " " * (4 - len(str(cone[0]))), ":",
              cone[1], " " * (13 - len(cone[1])), ":",
              cone[2], " " * (4 - len(str(cone[2]))), ":")


def print_scope_flavours():
    scope_flavours_list = [[1, 'Vanilla', 0.5], [2, 'Strawberry', 0.5],
                           [3, 'Chocolate', 0.5], [4, 'Caramel', 0.5],
                           [5, 'Mint', 0.5], [6, 'Rainbow', 0.5],
                           [7, 'Coffee', 0.5], [8, 'Bubble Gum', 0.5]]

    print(": Item  : Name           : Price :")
    for scope in scope_flavours_list:
        print(":", scope[0], " " * (4 - len(str(scope[0]))), ":",
              scope[1], " " * (13 - len(scope[1])), ":",
              scope[2], " " * (4 - len(str(scope[2]))), ":")


def print_topping_choices():
    topping_choices_list = [[1, 'Peanuts', 0.75], [2, 'Caramel Sauce', 0.5],
                            [3, 'Rainbow Sprinkles', 0.5], [4, 'Pecan', 1],
                            [5, 'Chocolate Sprinkles', 0.5]]

    print(": Item  : Name              : Price :")
    for topping in topping_choices_list:
        print(":", topping[0], " " * (4 - len(str(topping[0]))), ":",
              topping[1], " " * (20 - len(topping[1])), ":",
              topping[2], " " * (4 - len(str(topping[2]))), ":")


# functions to customize the ice cream order

def scope_flavours_choice():
    while True:
        # now let the user choose the number of scopes
        user_scopes_amount = input("\nEnter the number of scopes you want for this ice cream. Maximum scopes is 3: ")

        if user_scopes_amount.isnumeric() and int(user_scopes_amount) <= 3:
            break
        else:
            print("\nEnter a number, it must be less than or equal to 3")
            continue

    ice_cream_scopes = []
    ice_cream_scopes_price = 0

    for scopes in range(int(user_scopes_amount)):
        print_scope_flavours()

        while True:
            user_scope_flavours = input("Choose the scope flavours for your ice cream: ")
            if user_scope_flavours.isnumeric() and (1 <= int(user_scope_flavours) <= 8):
                break
            else:
                print("\nEnter a number, it must be between 1 and 8")
                continue

        ice_cream_scopes.append(user_scope_flavours)
        ice_cream_scopes_price = 0.5 * (scopes+1)

        print("\nYou choose the following scopes: ")
        for scope in ice_cream_scopes:
            print("\t--> " + str(scope_flavours_dict[int(scope)]))

        print(ice_cream_scopes)
        print("The cost of the scopes is: " + str(ice_cream_scopes_price))

    return ice_cream_scopes_price, ice_cream_scopes


def toppings_choice():
    while True:
        user_topping_preference = input("Enter the number of toppings for your ice cream. Max is 4: ")

        if user_topping_preference.isnumeric() and int(user_topping_preference) <= 4:
            break
        else:
            print("\nEnter a number, it must be less than or equal to 4")
            continue

    ice_cream_toppings = []
    ice_cream_toppings_price = 0

    for toppings in range(int(user_topping_preference)):
        print_topping_choices()

        while True:
            user_topping_choice = input("Choose the toppings for your ice cream: ")

            if user_topping_choice.isnumeric() and (1 <= int(user_topping_choice) <= 5):
                break
            else:
                print("\nEnter a number, it must be between 1 and 5")
                continue

        ice_cream_toppings.append(user_topping_choice)

        print("\nYou choose the following toppings: ")
        for topping in ice_cream_toppings:
            print("\t--> " + str(topping_choices_dict1[int(topping)]))

        # print("You choose the following toppings: " + str(topping_choices_dict1[int(user_topping_choice)]))
        print(ice_cream_toppings)

        if int(user_topping_choice) == 1:
            topping_price = topping_choices_dict['Peanuts']
            ice_cream_toppings_price = ice_cream_toppings_price + topping_price
        elif int(user_topping_choice) == 2:
            topping_price = topping_choices_dict['Caramel Sauce']
            ice_cream_toppings_price = ice_cream_toppings_price + topping_price
        elif int(user_topping_choice) == 3:
            topping_price = topping_choices_dict['Rainbow Sprinkles']
            ice_cream_toppings_price = ice_cream_toppings_price + topping_price
        elif int(user_topping_choice) == 4:
            topping_price = topping_choices_dict['Pecan']
            ice_cream_toppings_price = ice_cream_toppings_price + topping_price
        elif int(user_topping_choice) == 5:
            topping_price = topping_choices_dict['Chocolate Sprinkles']
            ice_cream_toppings_price = ice_cream_toppings_price + topping_price
        else:
            print('Sorry, not in list')

        print("The total cost of the toppings is: " + str(ice_cream_toppings_price))

    return ice_cream_toppings_price, ice_cream_toppings


def ice_cream_order_list():
    if cone_type_dict1[1]:
        print("\n\nThe ICE CREAM IS AS FOLLOWS\n"
              ": Cone Type :    Scope Flavours :    Price\n",
              str(cone_type_dict1[1]), " " * 3, " : ",
              str(toppings_item), " " * (4 - len(toppings_item)), ":",
              str(final_price))

        final_ice_cream_item.append(cone_type_dict1[1])
        final_ice_cream_item.append(scope_item)
        final_ice_cream_item.append(toppings_item)
        final_ice_cream_item.append(final_price)

    elif cone_type_dict1[2]:
        print("\n\nThe ICE CREAM IS AS FOLLOWS\n"
              ": Cone Type :    Scope Flavours :    Price\n",
              str(cone_type_dict1[2]), " " * 3, " : ",
              str(toppings_item), " " * (4 - len(toppings_item)), ":",
              str(final_price))

        final_ice_cream_item.append(cone_type_dict1[2])
        final_ice_cream_item.append(scope_item)
        final_ice_cream_item.append(toppings_item)
        final_ice_cream_item.append(final_price)

    elif cone_type_dict1[3]:
        print("\n\nThe ICE CREAM IS AS FOLLOWS\n"
              ": Cone Type :    Scope Flavours :    Price\n",
              str(cone_type_dict1[3]), " " * 3, " : ",
              str(toppings_item), " " * (4 - len(toppings_item)), ":",
              str(final_price))

        final_ice_cream_item.append(cone_type_dict1[3])
        final_ice_cream_item.append(scope_item)
        final_ice_cream_item.append(toppings_item)
        final_ice_cream_item.append(final_price)

    else:
        print('wrong choice')


"""*************** WELCOME CUSTOMER TO THE STORE AND BEGIN TRANSACTIONS **************************"""
print("Hello! Welcome to Below Zero Ice Cream Store. To be of great service we would want to personalize your order")

# personalize order by taking the customer name and track it

while True:

    user_name = str(input('\nKindly enter your name here: '))

    if user_name.isalpha() and (len(user_name) > 3 or len(user_name) == 3):
        user_order_number = randint(1, 100)

        user_order = {user_name: user_order_number}
        print(str(user_name.upper()) + ", this is your order number: " + str(user_order[user_name]))
        break

    else:
        print("Enter a valid name, it should be at least 3 characters long")
        continue

while True:
    # get the no. of ice creams from the customer
    user_ice_cream_request = input('\nEnter the number of ice creams you want to purchase: ')

    if user_ice_cream_request.isnumeric() and int(user_ice_cream_request) <= 10:
        print("\nYou ordered " + str(user_ice_cream_request) + " ice creams. Let's now get their specific details")
        break
    else:
        print("\nEnter valid number.NB numbers only and order should be less than 10")
        continue

# start customizing each ice cream

ice_cream_number = 0
final_ice_cream_item = []
total_payable_price = 0
for ice_cream in range(int(user_ice_cream_request)):
    ice_cream_number += 1
    print("CUSTOMIZE YOUR ICE CREAM NUMBER: " + str(ice_cream_number))
    final_ice_cream_item.append(ice_cream_number)

    # user chooses the cone types
    print("\t\t*** CONE TYPES ***\nThis are the available cone types and their respective prices")

    # ****** display the cone types
    print_cone_type()

    while True:
        user_cone_preference = input("\nChoose the cone Type: ")

        if user_cone_preference.isnumeric() and (1 <= int(user_cone_preference) <= 3):
            print(str(user_cone_preference))

            if int(user_cone_preference) == 1:
                user_cone_price = cone_type_dict['Plain Cone']
                print("\nYou picked Plain Cone and the price is: " + str(
                    user_cone_price) + ". Now pick the number of scopes")

                # customer picks the scopes they want and their flavours
                scope_price, scope_item = scope_flavours_choice()
                updated_price = scope_price + user_cone_price
                print("Current total price is: " + str(updated_price))

                # customer picks the toppings they want and their flavours
                toppings_price, toppings_item = toppings_choice()
                final_price = toppings_price + updated_price
                print("The total price of the ice cream is: " + str(final_price))

                # create the order list for the customer
                ice_cream_order_list()

                total_payable_price = total_payable_price + final_price

            elif int(user_cone_preference) == 2:
                user_cone_price = cone_type_dict['Waffle Cone']
                print("\nYou picked Waffle Cone and the price is: " + str(
                    user_cone_price) + ". Now pick the number of scopes")

                # customer picks the scopes they want and their flavours
                scope_price, scope_item = scope_flavours_choice()
                updated_price = scope_price + user_cone_price
                print("Current total price is: " + str(updated_price))

                # customer picks the toppings they want and their flavours
                toppings_price, toppings_item = toppings_choice()
                final_price = toppings_price + updated_price
                print("The total price of the ice cream is: " + str(final_price))

                # create the order list for the customer
                ice_cream_order_list()

                total_payable_price = total_payable_price + final_price

            elif int(user_cone_preference) == 3:
                user_cone_price = cone_type_dict['Cup']
                print(
                    "\nYou picked a cup and the price is: " + str(user_cone_price) + ". Now pick the number of scopes")

                # customer picks the scopes they want and their flavours
                scope_price, scope_item = scope_flavours_choice()
                updated_price = scope_price + user_cone_price
                print("Current total price is: " + str(updated_price))

                # customer picks the toppings they want and their flavours
                toppings_price, toppings_item = toppings_choice()
                final_price = toppings_price + updated_price
                print("The total price of the ice cream is: " + str(final_price))

                # create the order list for the customer
                ice_cream_order_list()

                total_payable_price = total_payable_price + final_price
            else:
                print("Wrong choice")

            break

        else:
            print("Choose numeric values between 1 , 2, 3")
            continue

# create the final order list for the customer
print("\n\nThe ICE CREAM ORDER IS AS FOLLOWS\n")
print(final_ice_cream_item)

print("Pay Cashier " + str(total_payable_price) + ". Get your ice cream at the counter")

