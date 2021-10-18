#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
# 

# @lc code=start
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        prefix = [[0 for _ in range(n+1)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j+1] = prefix[i][j]+mat[i][j]
        print(prefix)
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                minrow = max(0, i-k)
                mincol = max(0, j-k)
                maxrow = min(m, i+k+1)
                maxcol = min(n, j+k+1)
                for z in range(minrow, maxrow):
                    res[i][j] += prefix[z][maxcol] - prefix[z][mincol]
        return res
                
                
# @lc code=end took 24 Minutes

