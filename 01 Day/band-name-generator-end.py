# Main function is called implicitly.
# https://www.youtube.com/watch?v=bNk14P3vsRk

## If you make imports from different modules, Python does not know which program is now the main program.
## For this reason, it is necessary to define which program is the main function.

# import keyboard

# The code is only executed if this file is actually executed.
if __name__ == "__main__":
    while True:
        print("Welcome to the Band Name Generator. \n")
        city = input("What's the name of the city you grew up in?\n")
        pet = input("What's your pet's name?\n")
        print("Your band name could be:\n"+str(city)+str(pet))