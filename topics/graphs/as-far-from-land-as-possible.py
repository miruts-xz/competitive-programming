class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        mx = 0
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            r, c, d = q.popleft()
            for i, j in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
                if 0 <= i < len(grid) and 0 <= j < len(grid) and (i, j) not in visited:
                    q.append((i, j, d + 1))
                    visited.add((i, j))
            mx = max(d, mx)
        return mx if mx else -1
