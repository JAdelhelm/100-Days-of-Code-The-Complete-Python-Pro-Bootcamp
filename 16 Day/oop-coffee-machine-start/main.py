from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

if __name__ == '__main__':
    try:
        print(logo)
        menu_1 = Menu()
        coffee_maker_1 = CoffeeMaker()
        money_machine_1 = MoneyMachine()

        while True:
            try:
                # Hinzufügen des Attributes 'name' zum order - Objekt
                order_name = input(f'What would you like to order? ({menu_1.get_items()}): ')
                if order_name == "off": break
                elif order_name == "report": 
                    coffee_maker_1.report()
                    money_machine_1.report()

                else:
                    order = menu_1.find_drink(order_name)
                    order.name = order_name
                    print(order.name)      

                    if (order.name in menu_1.get_items()) == True:
                        if coffee_maker_1.is_resource_sufficient(drink=order) == True:
                            if order.cost > money_machine_1.money_received:    
                                if money_machine_1.make_payment(order.cost) == False: break
                                else: coffee_maker_1.make_coffee(order); print("\n")
                        else:
                            # Print ressources that are missing
                            coffee_maker_1.is_resource_sufficient(drink=order)
            except:
                print("Please use a valid input.")
                        
    except:
        print("Please use a valid input.")