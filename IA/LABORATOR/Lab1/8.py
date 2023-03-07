""" 
    genereates all the numbers (in binary) from 1 to n (inclusive)

    time: O(n)
    space: O(1)
"""
def generateBinary(n: int) -> list:  
    return [bin(i)[2:] for i in range(1, n + 1)]
    

def test():
    print("Testing 8...")
    assert generateBinary(4) == ['1', '10', '11', '100']

    print("Tests passed!")

test()