"""
    Să se determine distanța Euclideană între două locații identificate prin perechi de numere. 
    De ex. distanța între (1,5) și (4,1) este 5.0
"""

from math import sqrt

"""
    returns the euclidian distance between two points given as tuples

    p1 - tuple (len 2)
    p2 - tuple (len 2)

    time: O(1)
    space: O(1)
"""
def distance(p1: tuple, p2: tuple) -> float:
    assert len(p1) == 2
    assert len(p2) == 2

    distX = p1[0] - p2[0]
    distY = p1[1] - p2[1]
    
    return sqrt(distX**2 + distY**2)

def test():
    print("Testing 2...")
    assert distance((1, 5), (4, 1)) == 5.0
    assert distance((1, 1), (1, 2)) == 1
    assert distance((1, 2), (2, 1)) == sqrt(2)
    assert distance((1, 1), (1, 1)) == 0

    print("Tests passed!")

test()