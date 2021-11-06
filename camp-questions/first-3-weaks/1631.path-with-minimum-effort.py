#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from typing import List
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        def isvalid(i, j):
            return 0 <= i < m and 0 <= j < n
        directions = (1, 0, -1, 0, 1)
        heap, visited = [(0, 0, 0)], [[False for _ in range(n)] for _ in range(m)]
        while heap:
            effort, row, col = heappop(heap)
            if visited[row][col]:
                continue
            visited[row][col] = True
            if (row, col) == (m-1, n-1):
                return effort
            for i in range(4):
                r, c = row+directions[i], col+directions[i+1]
                if isvalid(r, c) and not visited[r][c]:
                    heappush(heap, (max(effort, abs(heights[r][c]-heights[row][col])), r, c))
        

# @lc code=end

