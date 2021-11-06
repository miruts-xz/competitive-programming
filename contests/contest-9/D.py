from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from functools import lru_cache
import sys
def solve(nums):
    scores = nums.copy()
    max_so_far = 0
    for i in range(len(nums)-1, -1, -1):
        nxt = i+nums[i]
        if nxt < len(nums):
            scores[i] += scores[nxt]
        max_so_far = max(max_so_far, scores[i])
    return max_so_far

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        ans.append(solve(list(map(int, input().split()))))
    print(*ans, sep='\n')