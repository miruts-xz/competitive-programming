#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        visited = [[False]*n for _ in range(n)]
        def valid(i,j):
            for c in range(j):
                if visited[i][c]: return False
            for x, y in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
                if visited[x][y]: return False
            for x, y in zip(range(i+1, n), range(j-1, -1, -1)):
                if visited[x][y]: return False
            return True
        def backtrack(col, rem):
            nonlocal count
            if col == n:
                count += (rem == 0)
                return
            for row in range(n):
                if not valid(row, col): continue
                visited[row][col] = True
                backtrack(col+1, rem-1)
                visited[row][col] = False
        backtrack(0, n)
        return count


# @lc code=end
# @time=12m

