from game_data import data
from replit import clear
from art import logo,vs
import random
import time
COUNT = 0
if __name__ == "__main__":
    while True:
        print(logo+"\n")
        if COUNT > 0: print(f"You're right! Current score: {COUNT}\n")
        if COUNT > 5: print("YOU HAVE A RUN! *-*\n")

        picks = random.choices(data,k=2)
        pick_1 = picks[0]
        pick_2 = picks[1]
        
        
        name_1 = pick_1["name"]
        name_2 = pick_2["name"]

        follower_1 = pick_1["follower_count"]
        follower_2 = pick_2["follower_count"]
        
        description_1 = pick_1["description"]
        description_2 = pick_2["description"]

        country_1 = pick_1["country"]
        country_2 = pick_2["country"]

        print(f"Compare A: {name_1}, a {description_1}, from {country_1}.\n")
        print(vs+"\n")
        print(f"Against B: {name_2}, a {description_2}, from {country_2}.\n")

        pick_user = input("Who has more followers? Type 'A' or 'B': ") 

        if (pick_user == "A" and follower_1 > follower_2):
            COUNT += 1
        elif(pick_user == "B" and follower_2 > follower_1):
            COUNT += 1
        else:
            print(f"Sorry, that's wrong. Final score: {COUNT}!")
            COUNT = 0
            break
        clear()

















