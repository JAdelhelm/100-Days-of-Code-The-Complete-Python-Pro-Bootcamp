# Caesar Cipher - Always shift one letter further
### 1. get the index of the word in the text
### 2. get the index in the alphabet
### 3. shift the letter by corresponding entries


def decrypt(text="abracadabra", shift=5):
    if shift > 0:
        new_text = []
        for val in text:
            # Index from the text
            index = text.index(val)
            # Index of the letter from the alphabet
            new_index = alphabet.index(val)
            # Shift the letter in the alphabet by corresponding entries
            new_index = new_index + shift

            # Problem: At > 26 he has to start again from the beginning, i.e.
            if new_index >= 26: new_index = new_index % 26
            # Now I have the new index for the text, I have to parse it
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
            # Index from the text
            index = text.index(val)
            # Index of the letter from the alphabet
            new_index = alphabet.index(val)
            # Shift the letter in the alphabet by corresponding entries
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


