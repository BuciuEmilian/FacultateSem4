"""
    Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar 
    (care apare de mai mult de n / 2 ori). De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
"""

"""
    find the majority element in a given list

    l - list of ints

    time: O(n)
    space: O(1)
"""
def findMajority(l: list) -> int:
    votes = 0
    maj = -1

    for el in l:
        if votes == 0: 
            maj = el
            votes = 1
        else:
            if el == maj:
                votes += 1
            else:
                votes -= 1

    if checkMajority(l, maj):
        return maj
    else:
        return -1

def checkMajority(l: list, maj: int) -> bool:
    count = 0
    for el in l:
        if el == maj:
            count += 1

    return count > len(l) // 2

def test():
    print("Testing 6...")
    assert findMajority([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert findMajority([1, 2, 3, 4]) == -1
    
    print('Tests passed!')
    
test()