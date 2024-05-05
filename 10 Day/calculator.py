from art import logo
from replit import clear

print(logo)
calculation_log = ""

def next_number(number, operation):
    number_second = int(input("What's the next number?: "))
    global calculation_log
    calculation_log += str(number_second)

    clear()
    if operation == "+":  return number + number_second
    elif operation == "-":  return number - number_second
    elif operation == "*": return number * number_second
    elif operation == "/": return number / number_second
    elif operation == "**":  return number ** number_second


def calculator_first():
    number = int(input("What's the first number?: "))
    print("+\n-\n*\n/\n**")
    operation = input("Pick an operation: ")
    global calculation_log
    calculation_log += str(number) + " " + operation + " "


    return number, operation

result_of_calculation = 0
more_calc = True
try:
    first_number, operator = calculator_first()
    while more_calc == True:
        result_of_calculation = next_number(first_number, operator)
        print("The actual result is: ", result_of_calculation,"\n")

        
        check_next = input("Do you want to continue? (y/n): ")
        if check_next == "n": break
        print("+\n-\n*\n/\n**")
        operator = input("Pick an operation: ")
        calculation_log += " " + operator + " " 

        first_number = result_of_calculation
    print("The normal calculation result is: ", result_of_calculation)
    print()
    calculate = eval(calculation_log)
    print("Calculation log:", calculation_log, " = ", calculate)


except:
    print("The result is: ", result_of_calculation)
    print("Further calculation: ", calculation_log)




    


