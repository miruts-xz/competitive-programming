import sys
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = -sys.maxsize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    mx = max(self.dfs(grid, i, j), mx)
        return 0 if mx == -sys.maxsize else mx

    def dfs(self, grid: List[List[int]], r, c) -> int:
        grid[r][c] = 0
        res = 1
        tempr = r
        tempc = c
        for i in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            r = tempr + i[0]
            c = tempc + i[1]
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
                res += self.dfs(grid, r, c)
        return res
