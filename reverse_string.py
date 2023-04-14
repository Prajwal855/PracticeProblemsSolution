#cmethod 1
txt = 'Hello world'[::-1]
print(txt)


# method 2
def reverse(s):
    str = ""
    for i in s:
        str = i +str
    return str


s = input("Enter the Word to be reversed : \n")

print('The orignal Word you sent : \n')
print(s)
print('The reversed String : \n')
print(reverse(s=s))