def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(min(a, b), max(a, b) % min(a, b))


print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(12, 9))
print(gcdRecur(17, 12))
