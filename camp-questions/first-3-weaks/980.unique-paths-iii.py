#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
from typing import List
# import sys
from functools import lru_cache
# sys.setrecursionlimit(2000)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        obs = 0
        strow, stcol = 0, 0
        endrow, endcol = 0, 0
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == -1:
                    obs += 1
                elif cell == 1:
                    strow, stcol = r, c
                elif cell == 2:
                    endrow, endcol = r, c
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        NON_OBSTACLES = m*n-2-obs
        DIR = (1, 0, -1, 0, 1)
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[strow][stcol] = True
        ans = 0
        def dfs(i, j, walks)->int:
            nonlocal ans
            print(f'row: {i} col: {j} walks: {walks}')
            if (i, j) == (endrow, endcol):
                if walks == NON_OBSTACLES+1: ans += 1
                return
            for t in range(4):
                newr, newc = i+DIR[t], j+DIR[t+1]
                if not valid(newr, newc) or grid[newr][newc] == -1  or visited[newr][newc]: continue
                visited[newr][newc] = True
                dfs(newr, newc, walks+1)
                visited[newr][newc] = False
        dfs(strow, stcol, 0)
        return ans
print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))

# @lc code=end

