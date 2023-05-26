def sub_string(word, substrings):
    substring_count = {}
    for substring in substrings:
        count = word.count(substring)
        if count > 0:
            substring_count[substring] = count
    return substring_count


if __name__ == '__main__':
    word = "Hello, Dude! How Are You?"
    sub_strings = ['Hello', 'Are', 'You']
    result = sub_string(word=word, substrings=sub_strings)
    print(result)