"""
    Să se determine cuvintele unui text care apar exact o singură dată în acel text. 
    De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
"""


"""
    finds the words that appear only once in a text

    text - str

    time: O(n)
    space: O(n)
"""
def findUniqueWords(text: str) -> set:
    # I could get rid of the extra space by iterating over the text directly, but the time 
    # performance might be poorer (not asymptotically - complexity stays the same).
    
    # Also space complexity will stay O(n) since all the words could be unique, in which case 
    # I'd have to store them all in the resulting set.

    words = text.split(" ") 
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    return {word for (word, count) in dict.items() if count == 1}

def test():
    print("Testing 4...")
    assert findUniqueWords('ana are ana are mere rosii ana') == {'mere', 'rosii'}
    assert findUniqueWords('ana ana ana mere mere') == set()
    assert findUniqueWords('ana are mere') == {'ana', 'are', 'mere'}

    print("Tests passed!")

test()