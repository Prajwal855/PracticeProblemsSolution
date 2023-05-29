def truncate_to_number(num):
    return round(num / 1000) * 1000


if __name__ == '__main__':
    num = int(input("Enter The Number (1000-9999) : "))
    truncated = truncate_to_number(num=num)
    print(truncated)