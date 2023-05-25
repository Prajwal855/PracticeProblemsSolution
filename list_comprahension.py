import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

find = 3

z = [val for num in x for val in num if val == find]

s = [1, 2, 3, 4, 5, 6]

q = [n for n in s]

y = np.array(x)

print(x)
print("-"*10)
print("Using numpy")
print(y)
print("-"*10)
print("Using List Compraheion")
print(q)
print("-"*10)
print("Using List Compraheion")
print(z)