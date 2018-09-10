def scope_flavours_choice():
    # now let the user choose the number of scopes
    user_scopes_amount = input("Enter the number of scopes you want for this ice cream. Maximum scopes is 3: ")

    ice_cream_scopes = []
    ice_cream_scopes_price = 0

    for scopes in range(int(user_scopes_amount)):
        user_scope_flavours = int(input("Choose the scope flavours for your ice cream: "))

        ice_cream_scopes.append(user_scope_flavours)
        # print("You choose the following flavours: " + str(scope_flavours_dict[user_scope_flavours]))
        print(ice_cream_scopes)

        ice_cream_scopes_price = 0.5 * (scopes + 1)
        print("The cost of the scopes is: " + str(ice_cream_scopes_price))

    return ice_cream_scopes_price


a = scope_flavours_choice()

print("this is the value of the function " + str(a))
