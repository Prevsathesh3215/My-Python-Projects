import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter : row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")
    try:
        word_nato = [new_dict[letter] for letter in word.upper()]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(word_nato)

generate_phonetic()