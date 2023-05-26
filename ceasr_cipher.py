import string


def caesar_cipher(text, shift):
    encoded_text = ''
    for letter in text:
        if letter.isalpha():
            start = ord('a')
            end = ord('z')
            encoded_letter = chr((ord(letter) - start + shift) % (end - start + 1) + start)
            encoded_text += encoded_letter
        else:
            encoded_text += letter

    return encoded_text


if __name__ == '__main__':
    text = str(input("Enter the Text To be Encoded : ")).lower()
    shift = int(input("Enter The Shift From(1 - 9) : "))
    encode = caesar_cipher(text=text, shift=shift)
    print(encode)



