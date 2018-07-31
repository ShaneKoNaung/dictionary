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
        close_words = close(w, dict.keys(), cutoff=0.75)
        if len(close_words) > 0:
            print("Did you mean {} instead? Enter Y if yes , N if no.".format(close_words[0]))
            yn = input("Enter :")
            if yn == 'Y':
                return dict[close_words[0]]
            else:
                return "I don't understand your input."



def dictionary():
    word = input('Enter :')
    word = word.strip().lower()
    print(meaning(word))


dictionary()
