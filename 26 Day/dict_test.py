import pandas as pd


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df_nato = pd.read_csv("Day_26/NATOalphabet.csv", encoding="ISO-8859-1")

# print(df_nato.head(3))

# df_dict = {df_nato["letter"]:df_nato["code"][key] for key,value in df_nato.iterrows()}
# print(df_dict)

# ODER:
df_dict = {row.letter: row.code for (index,row) in df_nato.iterrows()}
print(df_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_user_input = str(input("NATO transformed word: ")).upper()

for letter in nato_user_input:
    print(f"{letter} wie: {df_dict[letter]}")
