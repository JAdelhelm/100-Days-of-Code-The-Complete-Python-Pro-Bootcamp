# Caesar Cipher - Immer um einen Buchstaben weiter shiften
### 1. Hole mir den Index des Wortes im Text
### 2. Hole mir den Index im Alphabet
### 3. Shifte den Buchstaben um entsprechende Einträge

def decrypt(text="abracadabra", shift=5):
    if shift > 0:
        new_text = []
        for val in text:
            # Index aus dem Text
            index = text.index(val)
            # Index des Buchstabens aus dem Alphabet
            new_index = alphabet.index(val)
            # Shifte den Buchstaben im Alphabet um entsprechende Einträge
            new_index = new_index + shift

            # Problem: Bei > 26 muss er wieder von vorne anfangen, heißt also    
            if new_index >= 26: new_index = new_index % 26
            # Jetzt habe ich den neuen Index für den Text, diesen muss ich parsen
            # Also: Text[Index] = Alphabet[Index]
            # print("New Index: ",new_index)
            new_text.append(alphabet[new_index])
            # text[index] = alphabet[new_index]
           
        print("Decyrpted word: " + "".join(new_text))
    else:
        print("Please use an allowed shift value")
    again = input("Do you want to restart? Type 'y': ")
    if again == "y": 
        shift, text =inputFunction()
        decrypt(text, shift)


def encrypt(text="abracadabra", shift=5):
    if shift > 0:
        new_text = []
        for val in text:
            # Index aus dem Text
            index = text.index(val)
            # Index des Buchstabens aus dem Alphabet
            new_index = alphabet.index(val)
            # Shifte den Buchstaben im Alphabet um entsprechende Einträge
            new_index = new_index - shift
            # print("New Index: ",new_index)
            new_text.append(alphabet[new_index])
            # text[index] = alphabet[new_index]
        print("Encrypted word: " + "".join(new_text))
    else:
        print("Please use an allowed shift value")
        
    again = input("Do you want to restart? Type 'y': ")
    if again == "y": 
        shift, text =inputFunction()
        decrypt(text, shift)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
def inputFunction():
    try:
        shift = int(input("Please enter the shift 1-26: "))
        word = input("Please enter the word: ").upper()
        word = [val for val in word]
        return shift, word
    except:
        print("Please check your input.")

shift, word = inputFunction()
if direction == "encode":
    encrypt(word, shift)
elif direction == "decode":
    decrypt(word, shift)


