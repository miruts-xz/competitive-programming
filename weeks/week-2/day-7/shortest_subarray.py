from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        ans = len(A) + 1
        sums = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            sums[i] = sums[i - 1] + A[i - 1]
        dq = deque()
        for i, v in enumerate(sums):
            while dq and dq[-1][1] >= v:
                dq.pop()
            while dq and v - dq[0][1] >= K:
                ans = min(i - dq[0][0], ans)
                dq.popleft()
            dq.append((i, v))
        return ans if ans <= len(A) else -1
