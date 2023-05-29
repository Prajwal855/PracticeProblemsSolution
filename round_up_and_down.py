def round_up_and_round_down(num):
    return round(num / 100) * 100


if __name__ == '__main__':
    num = int(input(" Enter the number from 1000 - 9999 :"))
    truncated = round_up_and_round_down(num=num)
    print(truncated)