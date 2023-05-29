"""Split the string into substrings of 3 characters each but do not take the space as a character while splitting"""


def split_letters(sentence):
    sentence = sentence.replace(' ','')
    for letter in range(0, len(sentence), 3):
        print(sentence[letter:letter+3])


sentence = 'Hey Dude Whatzapp'
split_letters(sentence=sentence)

