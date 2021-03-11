from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c] == 1:
                    q.append((r, c))
                    isWater[r][c] = 0
                    visited.add((r, c))
                else:
                    isWater[r][c] = 2 * len(isWater) + 1
        while q:
            r, c = q.popleft()
            mn = 2 * len(isWater) + 1
            for rn, cn in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]:
                if 0 <= rn < len(isWater) and 0 <= cn < len(isWater[0]):
                    if (rn, cn) not in visited:
                        q.append((rn, cn))
                        visited.add((rn, cn))
                    else:
                        mn = min(mn, isWater[rn][cn])
            if isWater[r][c] != 0:
                isWater[r][c] = mn + 1
        return isWater
