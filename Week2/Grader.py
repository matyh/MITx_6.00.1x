from math import *

def polysum(n, s):
    """
    :param n: int, number of sides of the regular polynome
    :param s: int, length of the polynom's side
    :return: sum of the area and square of the perimeter of the regular polygon
     rounded on 4 decimal places.
    """
    polyArea = (0.25 * n * s ** 2) / (tan(pi / n))
    polyPeri = n * s
    return round(polyArea + polyPeri ** 2, 4)


print(polysum(4, 2))
