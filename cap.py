"""Capitalise the starting letter of all words in a string sentence"""


def capitalize_the_sentence(sentence):
    return sentence.title()


if __name__ == '__main__':
    sentence = 'he ate an apple under a tree'
    updated_sentence = capitalize_the_sentence(sentence=sentence)
    print(updated_sentence)