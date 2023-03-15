import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

def generate_phonetic():
    try:
        user = input("Enter a word: ")
        results = [nato_dict[letter.upper()] for letter in user]
    except:
        print("Enter only alphabets please.")
        generate_phonetic()
    else:
        print(results)
        
    
generate_phonetic()
