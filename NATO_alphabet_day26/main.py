import pandas

# TODO 1. Create a dictionary in this format:
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:\n")
letters = [letter.upper() for letter in word]
nato_letters = [alphabet[letter] for letter in letters]
print(nato_letters)
