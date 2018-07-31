import json
from difflib import get_close_matches as close

dict = json.load(open('dictionary.json'))


def meaning(w):
    '''
    return the meaning(s) of the word w
    '''
    try:
        return dict[w]
    except KeyError:
        # guess the closest word
        close_words = close(w, dict.keys(), cutoff=0.75)
        if len(close_words) > 0:
            print("Did you mean {} instead? Enter Y if yes , N if no.".format(close_words[0]))
            yn = input("Enter :")
            while yn != 'Y' and yn != 'N':
                yn = input("Try agian(Y or N) :")
            if yn == 'Y':
                return dict[close_words[0]]
        else:
            return "I don't understand your input."


def print_words(words):
    if type(words) == str:
        print(words)
        return
    for i, w in enumerate(words):
        print("{}: {}".format(i+1, w))
    print("Enter q to quit.")
    print()



def dictionary():
    while True:
        word = input('Enter :')
        if word == 'q':
            break
        word = word.strip().lower()
        print_words(meaning(word))


dictionary()
