"""
    Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură valoare 
    se repetă de două ori, să se identifice acea valoare care se repetă. De ex. în șirul [1,2,3,4,2] 
    valoarea 2 apare de două ori.
"""

"""
    finds the duplicate number in a list (of length n) containing all numbers from {1, 2, ..., n - 1}

    l - list

    time: O(n)
    space: O(1)
"""
def findDuplicate(l: list) -> int:
    n = len(l)
    my_sum = n * (n - 1) // 2

    return sum(l) - my_sum

def test():
    print("Testing 5...")
    assert findDuplicate([1, 2, 3, 4, 2]) == 2
    assert findDuplicate([1, 3, 3, 4, 2]) == 3
    assert findDuplicate([1, 2, 1]) == 1

    print("Tests passed!")

test()