#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def can_place(row, col):
            for c in range(col):
                if board[row][c] == "Q":
                    return False
            for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[r][c] == "Q":
                    return False
            for r, c in zip(range(row, n), range(col, -1, -1)):
                if board[r][c] == "Q":
                    return False
            return True
        def _solveQueens(col):
            if col >= n:
                ans.append([''.join(l) for l in board])
            for row in range(n):
                if can_place(row, col):
                    board[row][col] = 'Q'
                    _solveQueens(col+1)
                    board[row][col] = '.'
        _solveQueens(0)
        return ans
# @lc code=end

