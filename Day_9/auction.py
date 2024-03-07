# Cleart die Konsole
from replit import clear
# name = Key
# bid  = value
# Dictionary
from art import logo
name_bid = {}
bidder_counter = 1

print("Welcome to the secret auction program!")


def start_program():
    print(logo)
    start_name = input("What is your name?: ")
    start_bid = int(input("What is your bid?: $"))
    name_bid[bidder_counter] = {"Name": start_name, "Gebot": start_bid}
    clear()


def append_bidders():
    global bidder_counter
    bidder_counter += 1
    name_bidder = input("What is your name? ")
    bid_of_bidder = int(input("What is your bid?: $"))
    name_bid[bidder_counter] = {"Name": name_bidder, "Gebot": bid_of_bidder}
    


start_program()

check_more_bidders = input("Are there more bidders? (y/n): ")

while check_more_bidders == "y" or check_more_bidders == "Y":
    append_bidders()
    clear()
    check_more_bidders = input("Are there more bidders? (y/n): ")

winner = ""
highest = 0
for entry in name_bid.keys():
    if name_bid[entry]["Gebot"] >= highest:
        highest = name_bid[entry]["Gebot"]
        winner = name_bid[entry]["Name"]


print(f"The winner is {winner} with a bid of ${highest}.")


