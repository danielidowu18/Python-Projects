from maker_menu import MENU, resources

def extra_buttons(maker_button):
    global offMaker
    if maker_button == "report":
        print(resources)
    elif maker_button == "off":
        offMaker = True
def coins():
    global quarters, dimes, nickles, pennies, total
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
def check_money(total, fee):
    global remainder
    if total > fee:
        remainder = round(total - fee, 2)
        print(f"Here is ${remainder} in change.")
        print(f"Here is your {maker_button} ☕ Enjoy!")
    elif total == fee:
        print(f"Here is your {maker_button} ☕ Enjoy!")
    elif total < fee:
        print("Sorry that's not enough money. Money Refunded")
def check_resources(coffee_water, coffee_milk, coffee_coffee, maker_water, maker_milk, maker_coffee, maker_money, fee):
    global insufficient_resources
    if coffee_water > maker_water:
        print("Sorry there is not enough water.")
        insufficient_resources = True
    elif coffee_milk > maker_milk:
        print("Sorry there is not enough milk.")
        insufficient_resources = True
    elif coffee_coffee > maker_coffee:
        print("Sorry there is not enough coffee")
        insufficient_resources = True
    else:
        resources["water"] -= coffee_water
        resources["milk"] -= coffee_milk
        resources["coffee"] -= coffee_coffee
        resources["money"] += fee        
     
offMaker = False
quarters = 0
dimes = 0
nickles = 0
pennies = 0
total = 0
remainder = 0
insufficient_resources = False
while not offMaker:
    maker_button = input("What would you like? (espresso/latte/cappuccino): ").lower()
    extra_buttons(maker_button)
    if maker_button != "report" and maker_button != "off":
        coffee_water = MENU[maker_button]["ingredients"]["water"]
        coffee_milk = MENU[maker_button]["ingredients"]["milk"]
        coffee_coffee = MENU[maker_button]["ingredients"]["coffee"]
        maker_water = resources["water"]
        maker_milk = resources["milk"]
        maker_coffee = resources["coffee"]
        maker_money = resources["money"]
        fee = MENU[maker_button]["cost"]
        insufficient_resources = False
        check_resources(coffee_water, coffee_milk, coffee_coffee, maker_water, maker_milk, maker_coffee, maker_money, fee)
    if insufficient_resources == False:
        if maker_button == "espresso":       
            print("Please insert coins.")
            coins()
            check_money(total, fee)
        elif maker_button == "latte":
            print("Please insert coins.")
            coins()
            check_money(total, fee)
        elif maker_button == "cappuccino":
            print("Please insert coins.")
            coins()
            check_money(total, fee) 
