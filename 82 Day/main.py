#%%
import pandas as pd

class MorseCodeConverter: 
    def __init__(self, string_to_morse) -> None:
        self.string_to_morse = string_to_morse.replace(" ", "")
        self.string_to_morse_transformed = ""


    def transform_string_to_morse(self):
        df = pd.read_csv("./morse.csv", sep=",", names=["Alphabet", "Morse"])
        df = pd.Series(index=df.Alphabet, data=df.Morse.values).to_dict()
        
        self.string_to_morse_transformed
        for character in self.string_to_morse:
            self.string_to_morse_transformed += df[character.upper()] + " "

        print(self.string_to_morse_transformed) 
    
    def transform_morse_to_string(self, morse_code):
        df = pd.read_csv("./morse.csv", sep=",", names=["Alphabet", "Morse"])
        df = pd.Series(index=df.Morse, data=df.Alphabet.values).to_dict()

        # Split, because of the spaces
        morse_code = morse_code.split()

        morse_to_string = ""
        for character in morse_code:
            morse_to_string += df[character.strip()]

        print(morse_to_string)

        return morse_to_string   



if __name__ == "__main__":
    # Transforms string to morse
    morse_converter = MorseCodeConverter("Hey this is a morse code test")
    morse_converter.transform_string_to_morse()

    # Transforms morse back to string
    morse_code  = morse_converter.string_to_morse_transformed
    morse_converter.transform_morse_to_string(morse_code)