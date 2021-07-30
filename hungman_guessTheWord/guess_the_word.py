import random
from words import words
import string

def clean_list(inp):
    y = []
    for i in inp:
        if "-" not in inp or " " not in inp:
            i = y.append(i)
    ret = random.choice(y)
    print(ret)
    return ret.upper()

def act_game():

    get_word = clean_list(words)
    word_letter = set(get_word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    guess_limit = 6
    while len(word_letter) > 0 and guess_limit > 0:
        print("you have", guess_limit, "life left" "you have user these letter:- ", " ".join(used_letter))

        word_dash = [letter if letter in used_letter else '-' for letter in get_word]
        print('Current word: ', ' '.join(word_dash))
        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                live = live - 1
        elif user_input in used_letter:
            print("you have alredy used this letter: ")
        else:
            print("invalid input/character")

    if guess_limit == 0:
        print("you are out!, correct word was "+ get_word)
    else:
        print("congrats you win!! , guessed the right word "+ get_word)
act_game()
