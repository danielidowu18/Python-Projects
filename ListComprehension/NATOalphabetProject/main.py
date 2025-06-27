import pandas 
data = pandas.read_csv("./ListComprehension/NATOalphabetProject/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# OR
# for (index, row) in data.iterrows():
#     alphabet_dict.update({row.letter: row.code})
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

try:
    nato_user_word_list = [alphabet_dict[letter] for letter in user_word]
    # OR
    # for letter in user_word:
    #     nato_user_word_list.append(alphabet_dict[letter])
except KeyError:
    is_keyerror = True
    while is_keyerror:
        print("Sorry, only letters in the alphabet")
        user_word = input("Enter a word: ").upper()
        try:
            nato_user_word_list = [alphabet_dict[letter] for letter in user_word]
        except KeyError:
            pass
        else:
            is_keyerror = False
    print(nato_user_word_list)
else:
    print(nato_user_word_list)
