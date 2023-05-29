
def replace_word_number(sentence):
    word_numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    words = sentence.split()
    for i in range(len(words)):
        word = words[i].lower()
        if word in word_numbers:
            words[i] = word_numbers[word]

    return ' '.join(words)


sentence = "There are two shops near our area"
result = replace_word_number(sentence=sentence)
print(result)
