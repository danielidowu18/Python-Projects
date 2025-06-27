from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menus = Menu()

# coffee_name = MenuItem.__name__
# coffee_cost = MenuItem
# coffee_ingredients = MenuItem.ingredients
# coffee_water = coffee_ingredients["water"]
# coffee_milk = coffee_ingredients["milk"]
# coffee_coffee = coffee_ingredients["coffee"]
# menu_items = MenuItem(coffee_name, coffee_water, coffee_milk, coffee_coffee, coffee_cost)

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
if choice == "report":
        print(maker.report())
        print(money.report())
elif choice == "off":
        offMaker = True