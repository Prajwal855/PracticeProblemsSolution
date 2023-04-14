def check_palindrome(word):
    if word == word[::-1]:
        print("The Word Is Palindrome")
    else:
        print("It is not a Palindrome")
    pass


word = input("Enter any Word : ")
print(check_palindrome(word=word))
