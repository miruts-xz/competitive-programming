#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        occupied = set()
        def parallel(p1,p2, x, y)->bool:
            # print(p1,p2,x,y)
            slope = (y-p2)/(x-p1)
            print(slope)
            return slope != 1.0 and slope != -1.0
        ans = []
        def valid(i,j):
            return 0<=i<n and 0<=j<n
        def can_place(i,j):
            return all([i != r and j != c and not parallel(i,j,r,c) for r,c in occupied])
        def _solveNQueens(j,m)->bool:
            if j == n:
                return False
            if m == 0:
                ans.append(list(occupied))
                return True
            for i in range(n):
                if can_place(i,j):
                    occupied.add((i,j))
                    _solveNQueens(j+1,m-1)
                    occupied.remove((i,j))
        for j in range(n):
            occupied.add((0,j))
            _solveNQueens(j,n-1)
            occupied.remove((0,j))
        print(ans)               
        
# @lc code=end

