# Created by miruts on 8/16/2021. Copyright 2021, All rights reserved.
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                elif matrix[i][j] == 0:
                    r = i
                    c = j
                    for k in range(n):
                        if matrix[r][k] != 0:
                            visited.add((r, k))
                        matrix[r][k] = 0

                    for k in range(m):
                        if matrix[k][c] != 0:
                            visited.add((k, c))
                        matrix[k][c] = 0


if __name__ == '__main__':
    print(Solution().setZeroes([[1, 0, 2], [0, 2, 2], [1, 1, 0]]))
