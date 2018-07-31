import json

dict = json.load(open('dictionary.json'))


def meaning(w):
    '''
    return the meaning(s) of the word w
    '''
    try:
        return dict[w]
    except KeyError:
        return 'Invalid word'


def dictionary():
    word = input('Enter :')
    word = word.strip().lower()
    print(meaning(word))


dictionary()
