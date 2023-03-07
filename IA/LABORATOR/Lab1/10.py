"""
    Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice indexul 
    liniei care conține cele mai multe elemente de 1.
"""

"""
    returns the index of the row (of a matrix containing 0s and 1s with lines sorted increasingly) with the most 1s

    time: O(n + m)
    space: O(1)
"""
def getBestRow(m: list) -> int:
    col = len(m[0]) - 1
    ans = 0
    for i in range(len(m)):
        while col >= 0 and m[i][col] == 1:
            col -= 1
            ans = i
        if col < 0:
            break

    return ans

def test():
    print("Testing 10...")
    m = [[0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,1,1,1]]
    assert getBestRow(m) == 1

    print("Tests passed!")

test()