class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        commonValueSet = intSet()
        if len(self.vals) == 0 or len(other.vals) ==0:
            return commonValueSet
        else:
            for e in self.vals:
                if e in other.vals:
                    commonValueSet.insert(e)
            return commonValueSet

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        """Returns the length of the set.
           This method is called by the `len` built-in function."""
        return len(self.vals)


s1 = intSet()
s1.insert(1)
s1.insert(3)
s1.insert(6)
s1.insert(7)
s1.insert(8)
s2 = intSet()
s2.insert(2)
s2.insert(3)
s2.insert(5)
s2.insert(7)

print(s1)
print(s2)
print(len(s1))
print(s1.intersect(s2))
