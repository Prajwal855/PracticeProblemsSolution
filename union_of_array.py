arr = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6, 7, 8]

union_arr = []

for i in arr:
    if i not in union_arr:
        union_arr.append(i)

for j in arr2:
    if j not in union_arr:
        union_arr.append(j)

if __name__ == '__main__':
    print(union_arr)