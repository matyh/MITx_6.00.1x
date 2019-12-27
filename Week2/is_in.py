def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return aStr == char
    middle = len(aStr) // 2
    if char == aStr[middle]:
        return True
    elif char > aStr[middle]:
        return isIn(char, aStr[middle:])
    elif char < aStr[middle]:
        return isIn(char, aStr[0:middle])


print("1", isIn("a", "abcdghij"))
print("2", isIn("g", "acdgij"))
print("3", isIn("g", "acdgi"))
print("4", isIn("g", "acdiklost"))
print("5", isIn("t", "acdiklost"))
print("6", isIn("g", ""))
