#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
from typing import List
from heapq import heappop, heappush
from collections import namedtuple

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n, trapped, heap, DIR = len(heightMap), len(heightMap[0]), 0, [], (1, 0, -1, 0, 1)
        visited = [[0 for _ in range(n)] for _ in range(m)]
        State = namedtuple('State', ('bound', 'row', 'col'))
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        for i in range(m):
            heappush(heap, State(heightMap[i][0], i, 0))
            heappush(heap, State(heightMap[i][-1], i, n-1))
            visited[i][0], visited[i][-1] = 1, 1
        for j in range(n):
            heappush(heap, State(heightMap[0][j], 0, j))
            heappush(heap, State(heightMap[-1][j], m-1, j))
            visited[0][j], visited[-1][j] = 1, 1
        while heap:
            curr = heappop(heap)
            trapped += curr.bound - heightMap[curr.row][curr.col]
            for i in range(4):
                newr, newc = curr.row+DIR[i], curr.col+DIR[i+1]
                if not valid(newr, newc) or visited[newr][newc]: continue
                visited[newr][newc] = 1
                heappush(heap, State(max(heightMap[newr][newc], curr.bound), newr, newc))
        return trapped
print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
# @lc code=end

