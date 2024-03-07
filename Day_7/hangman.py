from ascii_hangman import HANGMANPICS, logo

import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

lives = random.randint(1,7)
print(logo)
while True:
    rand_pick_word = random.choice(words)
    rand_pick_word = [val for val in rand_pick_word]

    letter_list = ["_" for val in range(len(rand_pick_word))]
    win = True
    counter = 0
    while "_" in letter_list:
        hangman = HANGMANPICS[counter]
        print(" ".join(letter_list))
        print(hangman)

        choose_letter = input("Guess a letter: ").lower()
        if choose_letter not in rand_pick_word:
            counter += 1
            print(counter, len(rand_pick_word))
            if counter == len(rand_pick_word):
                win = False
                break
        elif choose_letter in rand_pick_word:
            for position in range(len(rand_pick_word)):
                if rand_pick_word[position] == choose_letter:
                    letter_list[position] = choose_letter

        if choose_letter == "#":
            break
    print(" ".join(letter_list)+"\n")

    if win == True:
        print(f"Your word was " + "".join(rand_pick_word)+". You won!")
        print(f"You have {lives} lives left.\n")
    else:
        print(f"Your word was " + "".join(rand_pick_word)+". You lost!")
        lives -= 1
        print(f"You have {lives} lives left.\n")
        print("If you want to quit the game, type 'quit'.")
        user_input = input()
        if user_input == "quit":
            break

     
