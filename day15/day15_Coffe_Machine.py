on_or_off = "on"
water = 300
milk = 200
coffe = 100
choice_coffe = "on"
while choice_coffe != "off":
    choice_coffe = input("What would you like? (espresso/latte/cappuccino): ")

    if choice_coffe == "report":
        print(f"Water = {water}ml \n Milk = {milk}ml\nCoffe = {coffe}g")

    elif choice_coffe == "fill":
        water = 300
        milk = 200
        coffe = 100

    elif choice_coffe == "espresso":
        if water >= 50 and coffe >= 18:
            print("Please inser the coins : ")
            quarters = int(input("How many quarters : "))
            dimes = int(input("How many dimes : "))
            nickles = int(input("How many nickles : "))
            pennies = int(input("How many pennies : "))
            money = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
            if money >= 1.5:
                change = round(money - 1.5, 2)
                print(f"Here is in change ${change}")
                print("Enjoy your coffe ☕")
                water -= 50
                coffe -= 18
                print(f"Water = {water}ml \n Milk = {milk}ml\nCoffe = {coffe}g")
            else:
                print("Sorry that's not enough money. Money refunded. ")
        else:
            print("Sorry not enough ingredients ")

    elif choice_coffe == "latte":
        if water >= 200 and coffe >= 24 and milk >= 150:
            print("Please inser the coins : ")
            quarters = int(input("How many quarters : "))
            dimes = int(input("How many dimes : "))
            nickles = int(input("How many nickles : "))
            pennies = int(input("How many pennies : "))
            money = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
            if money >= 1.5:
                change = round(money - 2.5, 2)
                print(f"Here is in change ${change}")
                print("Enjoy your coffe ☕")
                water -= 200
                coffe -= 24
                milk -= 150
                print(f"Water = {water}ml \n Milk = {milk}ml\nCoffe = {coffe}g")
            else:
                print("Sorry that's not enough money. Money refunded. ")
        else:
            print("Sorry not enough ingredients ")

    elif choice_coffe == "cappuccino":
        if water >= 250 and coffe >= 24 and milk >= 100:
            print("Please inser the coins : ")
            quarters = int(input("How many quarters : "))
            dimes = int(input("How many dimes : "))
            nickles = int(input("How many nickles : "))
            pennies = int(input("How many pennies : "))
            money = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
            if money >= 3.0:
                change = round(money - 3.0, 2)
                print(f"Here is in change ${change}")
                print("Enjoy your coffe ☕")
                water -= 250
                coffe -= 24
                milk -= 100
                print(f"Water = {water}ml \n Milk = {milk}ml\nCoffe = {coffe}g")
            else:
                print("Sorry that's not enough money. Money refunded. ")
        else:
            print("Sorry not enough ingredients ")
