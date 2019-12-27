import math, time


def isPrime(n):
    """
    :param n: int, number to check if prime
    :return: boolean whether prime or not
    """
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    return True


def genPrimes():
    number = 0
    while True:
        if isPrime(number):
            yield number
        number += 1


def genPrimes2():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


start = time.time()
for i in genPrimes():
    # print(i)
    if i == 2978869:
        print("Time:", time.time() - start)
        break

start = time.time()
for i in genPrimes2():
    if i == 2978869:
        print("Time:", time.time() - start)
        break
