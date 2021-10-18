#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        def valid(i,j):
            return 0<=i<m and 0<=j<n
        def dfs(i, j):
            DIR = (1, 0, -1, 0, 1)
            maxx = mat[i][j]
            nr, nc, = i, j
            for k in range(4):
                r, c = DIR[k]+i, DIR[k+1]+j
                if valid(r, c):
                    if mat[r][c] > maxx:
                        nr, nc = r, c
            if nr != i or nc != j:
                return dfs(nr, nc)
            return [i, j]
        return dfs(0,0)
                
                    
# @lc code=end

