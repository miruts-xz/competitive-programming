#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from heapq import heappop, heappush
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        linear, squares = [i for i in range(n*n, 0, -1)], []
        l, r, turn = 0, n, 0
        while r <= n*n:
            if n % 2 == 0:
                squares.append(linear[l:r][::-1] if turn else linear[l:r])
            else:
                squares.append(linear[l:r] if turn else linear[l:r][::-1])
            l, r, turn = l + n, r+n, turn^1
        num_to_index = [0]*((n*n)+1)
        print(squares)
        for i in range(n):
            for j in range(n):
                num_to_index[squares[i][j]] = (i,j)
        # print(num_to_index)
        del squares
        del linear
        heap = [(0, -1, False)]
        visited = set()
        while heap:
            steps, cur, took = heappop(heap)
            cur = abs(cur)
            print(steps, cur)
            if cur == n*n:
                return steps
            visited.add(cur)
            for i in range(cur+1, min(n*n, cur+6)+1):
                if i not in visited:
                    # print(num_to_index[i])
                    ii, jj = num_to_index[i]
                    to = i if board[ii][jj] == -1 else i
                    if to not in visited and to != -1 and not took:
                        heappush(heap, (steps+1, -board[ii][jj], True))
                    else:
                        heappush(heap, (steps+1, -i, False))
        return -1
print(Solution().snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
# @lc code=end

