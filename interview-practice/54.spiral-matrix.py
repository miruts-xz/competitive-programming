#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from math import ceil
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        if m == 1: return matrix[0]
        if n == 1: return [i for ls in matrix for i in ls]
        spirals = ceil(min(m,n)/2)
        def spiral(l=0, results=[]):
            if l == spirals: return
            if l == spirals-1 and min(m,n)%2:
                if n > m:
                    for col in range(l, n-l):
                        results.append(matrix[l][col])
                else:
                    for row in range(l, m-l):
                        results.append(matrix[row][n-1-l])
                return
            for col in range(l, n-1-l):
                results.append(matrix[l][col])
            for row in range(l, m-1-l):
                results.append(matrix[row][n-1-l])
            for col in range(n-1-l, l, -1):
                results.append(matrix[m-1-l][col])
            for row in range(m-1-l, l, -1):
                results.append(matrix[row][l])
            spiral(l+1,results)
        results = list()
        spiral(0,results)
        return results
            

# @lc code=end

