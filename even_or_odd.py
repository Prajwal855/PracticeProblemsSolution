def even_or_odd(num):
    if num % 2 == 0:
        print('The Number is Even')
    else:
        print('The Number is Odd')
    pass


num = int(input('Enter the number ?\n'))
print(even_or_odd(num=num))
