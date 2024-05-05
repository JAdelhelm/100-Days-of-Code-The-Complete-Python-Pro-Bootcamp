if __name__ == '__main__':
    #Write your code below this line 👇
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    percentage = float(input("What percentage tip would you like to give? 10,12, or 15? "))
    people = float(input("How many people to split the bill? "))

    calc = (bill * (1+(percentage/100))) / people
    print(f"Each person should pay: ${round(calc,2)}")