import random
from replit import clear
from logo import art
print(art)
print(
"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.  
"""
)
def run_game(attempts):
    number = random.randint(1, 100)
    while attempts > 0:
            if attempts == 0:
                print("\nYou lost.")
                break
            guess = int(input("Guess a number between 1 and 100. \n"))
            if guess > 100 or guess < 1: print("Please enter a number between 1 and 100.")
            else:
                print(f"\nYou have {attempts} attempts left.")
                if guess > number:
                    print("Too high.")
                elif guess < number:
                    print("Too low.")
                elif guess == number:
                    print("\nYou won!")
                    break
                attempts -= 1

while True:
    level  = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        attempts_hard = 5
        run_game(attempts_hard)
    elif level == "easy":
        attempts_easy = 10
        run_game(attempts_easy)
    one_more_game = input("\nWould you like to play another game? Type 'yes' or 'no': ").upper()
    if one_more_game != "YES":
        break
    clear()

        



