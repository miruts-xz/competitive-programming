from typing import List
from collections import deque


def shortest_sub_array(A: List[int], K: int) -> int:
    ans = len(A) + 1
    sums = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        sums[i] = sums[i - 1] + A[i - 1]
    dq = deque()
    for i, v in enumerate(sums):
        print('queue', dq)
        while dq and dq[-1][1] >= v:
            dq.pop()
        while dq and dq[-1][1] - dq[0][1] >= K:
            ans = min(dq[-1][0] - dq[0][0], ans)
            dq.popleft()
        dq.append((i, v))
    return ans if ans <= len(A) else -1


print(shortest_sub_array([10, -10, -1, 12, 3, 2], 15))
