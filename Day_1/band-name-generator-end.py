# Main-Funktion wird implizit aufgerufen.
# https://www.youtube.com/watch?v=bNk14P3vsRk

## Wenn man imports von unterschiedlichen Modulen macht, dann weiß Python nicht, welches Programm jetzt das Main-Programm ist.
## Aus diesem Grund muss definiert werden, welches Programm die Main-Funktion ist.

import keyboard

# Der code wird nur ausgeführt, wenn tatsächlich diese Datei ausgeführt wird.
if __name__ == "__main__":
    while True:
        print("Welcome to the Band Name Generator. \n")
        city = input("What's the name of the city you grew up in?\n")
        pet = input("What's your pet's name?\n")
        print("Your band name could be:\n"+str(city)+str(pet))