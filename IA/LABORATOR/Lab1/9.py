"""
    Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe 
    din matrice ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.
"""


"""
    returns the sums of the submatrices represented by the pair of indices

    matrix - list of lists of same length
    coordinates - list of lists of pairs

    n = #rows 
    m = #columns 
    time: O(n * m) 
    space: O(n * m)
"""
def submatrixSums(matrix, coordinates):
    partialSums = []
    for i in range(len(matrix)):
        partialSums.append([0] * len(matrix[0]))

    # (0, 0)
    partialSums[0][0] = matrix[0][0]
    # first row
    for k in range(1, len(matrix[0])):
        partialSums[0][k] = partialSums[0][k - 1] + matrix[0][k]
    # first column
    for k in range(1, len(matrix)):
        partialSums[k][0] = partialSums[k - 1][0] + matrix[k][0]

    for i in range(1, len(matrix)):
        for j in range (1, len(matrix[0])):
            partialSums[i][j] = partialSums[i][j - 1] + partialSums[i - 1][j] - partialSums[i - 1][j - 1] + matrix[i][j]

    ans = []
    for p in coordinates:
        i1, j1, i2, j2 = p[0][0], p[0][1], p[1][0], p[1][1]
        ans.append(partialSums[i2][j2] - partialSums[i2][j1 - 1] - partialSums[i1 - 1][j2] + partialSums[i1 - 1][j1 - 1])
    return ans


def test():
    print("Testing 9...")
    m = [[0, 2, 5, 4, 1],
         [4, 8, 2, 3, 7],
         [6, 3, 4, 6, 2],
         [7, 3, 1, 8, 3],
         [1, 5, 7, 9, 4]]
    assert submatrixSums(m, [[(1, 1), (3, 3)], [(2, 2), (4, 4)]]) == [38, 44]

    print("Tests passed!")

test()