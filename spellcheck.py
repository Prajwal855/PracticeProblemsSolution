"""Write a spell check program to replace all 'a's with 'an's if the following word starts with a vowel"""


def spell_check(sentence):
    words = sentence.split()
    corrected_word = []

    for letters in range(len(words)):
        current_letter = words[letters]
        next_letter = words[letters+1] if letters +1 <len(words) else None

        if current_letter.lower() == 'a' and next_letter and next_letter[0].lower() in 'aeiou':
            corrected_word.append('an')
        else:
            corrected_word.append(current_letter)

    corrected_sentence = ' '.join(corrected_word)
    print(corrected_sentence)


if __name__ == '__main__':
    sentence = 'There is a monkey eating a apple'
    spell_check(sentence=sentence)

