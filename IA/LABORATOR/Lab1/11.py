"""
    Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate aparițiile elementelor egale 
    cu 0 care sunt complet înconjurate de 1.
"""

# direction vectors
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

"""
    
"""
def solve(A: list) -> list:
    n = len(A)
    m = len(A[0])

    for i in range(n):
        if A[i][0] == 0:
            dfs(i, 0, A)
        if A[i][m - 1] == 0:
            dfs(i, m - 1, A)

    for j in range(m):
        if A[0][j] == 0:
            dfs(0, j, A)
        if A[n - 1][j] == 0:
            dfs(n - 1, j, A)

    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
               A[i][j] = 1
            elif A[i][j] == 2:
                A[i][j] = 0

    return A 
        

"""
    checks if a position is in boundries (inside the matrix)

    A - matrix (list of lists)

    time: O(1)
    space: O(1)
"""
def valid(i: int, j: int, A: list) -> bool:
    n = len(A)
    m = len(A[0])

    return i >= 0 and i < n and j >= 0 and j < m

"""
    marks the 0s that are reachable from the border of the matrix

    n = #rows 
    m = #columns

    time: O(n * m)
    space: O(1)
"""
def dfs(i: int, j: int, A: list):
    A[i][j] = 2
    for k in range(4):
        new_i = i + di[k]
        new_j = j + dj[k]
        if valid(new_i, new_j, A) and A[new_i][new_j] == 0: 
            dfs(new_i, new_j, A)

def test():
    print("Testing 11...")
    A1 = [[1,1,1,1,0,0,1,1,0,1],
          [1,0,0,1,1,0,1,1,1,1],
          [1,0,0,1,1,1,1,1,1,1],
          [1,1,1,1,0,0,1,1,0,1],
          [1,0,0,1,1,0,1,1,0,0],
          [1,1,0,1,1,0,0,1,0,1],
          [1,1,1,0,1,0,1,0,0,1],
          [1,1,1,0,1,1,1,1,1,1]]
    
    A2 = [[1,1,1,1,0,0,1,1,0,1],
          [1,1,1,1,1,0,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,0,1],
          [1,1,1,1,1,1,1,1,0,0],
          [1,1,1,1,1,1,1,1,0,1],
          [1,1,1,0,1,1,1,0,0,1],
          [1,1,1,0,1,1,1,1,1,1]]
    assert solve(A1) == A2

    print("Tests passed!")

test()