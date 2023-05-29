"""For a given string print all the permutations of characters"""


def permutation(word, current =''):
    if len(word) == 0:
       print(current)
    else:
        for letter in range(len(word)):
            rem = word[:letter] + word[letter+1:]
            permutation(rem, current + word[letter])

if __name__ == '__main__':
    word = input("Enter the Word Dude : ")
    permutation(word=word)



