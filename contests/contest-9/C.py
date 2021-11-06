from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from functools import lru_cache
import math
def solve(n, k):
    elapsed, rem, cur, updated = 0, n-1, 1, 1
    while rem > 0 and updated < n:
        rem -= cur
        updated += cur
        cur = min(updated, k)
        elapsed += 1
        if cur == k and rem > 0:
            elapsed += rem//cur
            if rem%cur: elapsed
            rem = 0
    return elapsed

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    print(*ans, sep='\n')