# %%
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
eazy_letters = "".join([random.choice(letters) for letter in range(0,nr_letters)])
eazy_symbols = "".join([random.choice(symbols) for symbol in range(0, nr_symbols)])
eazy_numbers = "".join([random.choice(numbers) for number in range(0, nr_numbers)])

password_easy = eazy_letters+eazy_symbols+eazy_numbers
print(f"Easy Password: {password_easy}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = [val for val in password_easy]
password_hard = "".join([random.choice(password_easy) for val in range(0,len(password_easy)-1)])

print(f"Hard Password: {password_hard}")


# %%



