def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    newTup = ()
    for i in range(0, len(aTup), 2):
        newTup += (aTup[i],)
    return newTup


def oddTuples2(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    return aTup[::2]


a = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(a))
print(oddTuples2(a))