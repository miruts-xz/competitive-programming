# Created by miruts on 8/11/2021. Copyright 2021, All rights reserved.

from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited, queue, result = set(), deque([s]), s
        while queue:
            curr = queue.popleft()
            result = min(result, curr)
            one = "".join([str((int(c) + a) % 10) if i % 2 else c for i, c in enumerate(curr)])
            two = curr[b:] + curr[:b]
            for new in [one, two]:
                if new not in visited:
                    visited.add(new)
                    queue.append(new)
        return result


if __name__ == "__main__":
    print(Solution().findLexSmallestString("503192", 7, 2))
