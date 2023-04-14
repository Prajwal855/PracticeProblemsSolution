sentence = input('Enter the Sentence :\n').lower().replace(' ', '')

vowels = 0
consonants = 0

for char in sentence:
    if char in 'aeiou':
        vowels += 1
    else:
        consonants += 1

print("Number Of Vowels in Sentence: ", vowels)
print("Number of Consonants in Sentence: ", consonants)
