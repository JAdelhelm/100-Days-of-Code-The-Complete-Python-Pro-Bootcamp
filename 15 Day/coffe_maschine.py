from coffee_data import MENU, resources

RESSOURCES = resources

def print_report():
    print(f"""
    Water: {RESSOURCES['water']}\n
    Milk: {RESSOURCES['milk']}\n
    Coffee: {RESSOURCES['coffee']}\n
    Money: {RESSOURCES['money']}\n
    """)

def print_missing_ressources(ressource, coffee_type):
    missing = RESSOURCES[ressource] - MENU[str(coffee_type)]['ingredients'][ressource]
    print(f"Missing {missing} of {ressource} for {coffee_type}.")



def check_ingredients(picked):
    ingredient_status = []
    if RESSOURCES['water'] < MENU[str(picked)]['ingredients']['water']:
        print('Not enough water in machine.')
        print_missing_ressources('water', picked)
        ingredient_status.append(False)
        
    if str(picked) != "espresso" and RESSOURCES['milk'] < MENU[str(picked)]['ingredients']['milk']:
        print('Not enough milk in machine.')
        print_missing_ressources('milk', picked)
        ingredient_status.append(False)

    if RESSOURCES['coffee'] < MENU[str(picked)]['ingredients']['coffee']:
        print('Not enough coffee in machine.')
        print_missing_ressources('coffee', picked)
        ingredient_status.append(False)

    if False in ingredient_status: return False
    else: return True
 
def remove_ingredients(picked):
    RESSOURCES['water'] = RESSOURCES['water'] - MENU[str(picked)]['ingredients']['water']
    if picked != "espresso": RESSOURCES['milk'] = RESSOURCES['milk'] - MENU[str(picked)]['ingredients']['milk']
    RESSOURCES['coffee'] = RESSOURCES['coffee'] - MENU[str(picked)]['ingredients']['coffee']


def ressources_money(picked_coffee):
    # First check if enough ingredients in machine
    check_ress = check_ingredients(picked_coffee)

    if check_ress == True:
        sum_inserted = 0
        if RESSOURCES['money'] < MENU[str(picked_coffee)]['cost']:
            try:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: ")) * 0.01
                dimes = int(input("How many dimes?: ")) * 0.1
                nickles = int(input("How many nickles?: ")) * 0.05
                pennies = int(input("How many pennies?: ")) * 0.25

                sum_inserted = quarters + dimes + nickles + pennies
                RESSOURCES['money'] += sum_inserted
            except: return False

        if RESSOURCES['money'] > MENU[str(picked_coffee)]['cost']:
            change = RESSOURCES['money'] - MENU[str(picked_coffee)]['cost']
            
            # Remove costs of coffee from RESSOURCES + change
            RESSOURCES['money'] =  RESSOURCES['money'] - MENU[str(picked_coffee)]['cost']
            RESSOURCES['money'] = RESSOURCES['money'] - change

            print(f"Here is ${change} your change.")
        else: 
            change_back = sum_inserted
            RESSOURCES['money'] = RESSOURCES['money'] - sum_inserted
            print(f"Here is ${change_back} your money back.")
            return False


        remove_ingredients(picked_coffee)
        return True

    return False



if __name__ == "__main__":
    while True:
        print()
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice == "report": print_report()

        elif coffee_choice == "latte" or coffee_choice == "espresso" or coffee_choice == "cappuccino":
            money_inserted = ressources_money(coffee_choice)
            if money_inserted == True: print(f"Here is your {coffee_choice} Enjoy!")


