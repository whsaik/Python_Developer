import pandas as pd

#TODO 1. Create a dictionary in this format:
nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word: ")
results = [nato_dict[letter.upper()] for letter in user]
print(results)