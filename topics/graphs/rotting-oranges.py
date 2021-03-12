from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        minutes = 0
        while q:
            r, c, m = q.popleft()
            for i, j in [[r, c - 1], [r, c + 1], [r + 1, c], [r - 1, c]]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited and grid[i][j] == 1:
                    # print(fresh)
                    fresh.remove((i, j))
                    q.append((i, j, m + 1))
                    visited.add((i, j))
            minutes = max(minutes, m)
        return -1 if len(fresh) else minutes




