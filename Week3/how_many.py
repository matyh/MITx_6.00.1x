def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key in aDict.keys():
        count += len(aDict[key])
    return count


aDict = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],
         "d": ["donkey", "dog", "cat"]}
print(how_many(aDict))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    most = 0
    result = ""
    for key in aDict:
        if len(aDict[key]) > most:
            most = len(aDict[key])
            result = key
    return result

print(biggest(aDict))
