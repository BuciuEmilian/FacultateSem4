"""
    Să se determine produsul scalar a doi vectori rari care conțin numere reale. 
    Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea 
    oricâte dimensiuni. De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] 
    și [1,2,0,3,1] este 4.
"""

"""
    computes the dot product of 2 vectors (they need to have the same length)

    v1 - list of floats
    v2 - list of floats

    time: O(n)
    space: O(1)
"""
def dotProduct(v1: list, v2: list) -> float:
    assert len(v1) == len(v2)

    sum = 0
    for (el1, el2) in zip(v1, v2):
        sum += el1 * el2

    return sum

def test():
    print("Testing 3...")
    assert dotProduct([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert dotProduct([1, 2, 3], [1, 1, 1]) == 6
    assert dotProduct([1, 0, 0], [0, 1, 1]) == 0

    print('Tests passed!')

test()