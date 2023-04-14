series = [1, 5, 6, 7, 8, 9, 10]
missing_series = []

for i in range(series[0], series[-1]+1):
    if i not in series:
        missing_series.append(i)

if __name__ == '__main__':
    print("The Missing Element in the array is :", missing_series)
