from typing import List


def max_peak(is_water: List[List[int]]) -> List[List[int]]:
    r = 0
    c = 0
    found = False
    for i in range(len(is_water)):
        for j in range(len(is_water[0])):
            if is_water[i][j] == 1:
                if not found:
                    r = i
                    c = j
                    found = True
                is_water[i][j] = 0
            else:
                is_water[i][j] = 1

    visited = set()
    dfs(is_water, r, c, visited)
    return is_water


def dfs(is_water: List[List[int]], r, c, visited):
    if (r, c) in visited:
        return
    visited.add((r, c))
    if is_water[r][c] == 1:
        mn = float('inf')
        for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if 0 <= i < len(is_water) and 0 <= j < len(is_water[0]):
                mn = min(mn, is_water[i][j])
        is_water[r][c] = 1 + mn
    for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if 0 <= i < len(is_water) and 0 <= j < len(is_water[0]):
            dfs(is_water, i, j, visited)


print(max_peak([[0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0]]))
"""
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0]

[1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 2],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 0, 1, 1, 1, 1, 1]
"""
