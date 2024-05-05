# %%
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


try:
    choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    number = int(choose)
    
    rand_player = random.randint(0,2)
    rand_computer = random.randint(0,2)
    
    # Print Player
    if rand_player == 0:
        print(rock)
    elif rand_player == 1:
        print(paper)
    elif rand_player == 2:
        print(scissors)

    # Print Computer
    print("Computer chose:")
    if rand_computer == 0:
        print(rock)
    elif rand_computer == 1:
        print(paper)
    elif rand_computer == 2:
        print(scissors)
    
    # Possibilities 9 Combinations
    if rand_player == rand_computer:
        print("Draw.")
    ##
    elif rand_player == 0 and rand_computer == 1:
        print("You lose.")
    elif rand_player == 0 and rand_computer == 2:
        print("You win.")
    ##
    elif rand_player == 1 and rand_computer == 0:
        print("You win.")
    elif rand_player == 1 and rand_computer == 2:
        print("You lose.")
    ##
    elif rand_player == 2 and rand_computer == 0:
        print("You lose.")
    elif rand_player == 2 and rand_computer == 1:
        print("You win.")



except:
    print("Not a Number as input")

# %%



