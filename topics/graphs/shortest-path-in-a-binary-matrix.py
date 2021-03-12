from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque()
        n = len(grid)
        visited = set()
        r, c = 0, 0
        mn = sys.maxsize
        q.append((r, c, 1))
        visited.add((r, c))
        while q:
            r, c, d = q.popleft()
            for i, j in [[r - 1, c], [r - 1, c + 1], [r, c + 1], [r + 1, c + 1], [r + 1, c], [r + 1, c - 1], [r, c - 1],
                         [r - 1, c - 1]]:
                if self.inRange(grid, i, j) and (i, j) not in visited and grid[i][j] != 1:
                    visited.add((i, j))
                    q.append((i, j, d + 1))
            if (r, c) == (n - 1, n - 1):
                mn = min(mn, d)
        return mn if (n - 1, n - 1) in visited else -1

    def inRange(self, grid, i, j) -> bool:
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
