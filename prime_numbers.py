def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(arr):
    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The Prime Numbers in array are :\n", find_primes(arr=arr))
