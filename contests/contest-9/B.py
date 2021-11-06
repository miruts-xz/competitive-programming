from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from functools import lru_cache

def solve(boxes):
    dp = {}
    ans = ""
    def dfs(i, prev=None)->tuple:
        if i == len(boxes):
            return (0, "")
        if (i, prev) in dp:
            return dp[i, prev]
        if boxes[i] == '?':
            costb, paintb = dfs(i+1, "B")
            costr, paintr = dfs(i+1, "R")
            if prev == 'B':
                costb += 1
            if prev == 'R':
                costr += 1
            paintb = "B"+paintb
            paintr = 'R'+paintr
            if costb < costr:
                dp[i, prev] = (costb, paintb)
            else:
                dp[i, prev] = (costr, paintr)
        else:
            paintBox = dfs(i+1, boxes[i])
            if prev == boxes[i]:
                paintBox = (paintBox[0]+1, paintBox[1])
            paintBox = (paintBox[0], boxes[i]+paintBox[1])
            dp[i, prev] = paintBox
        return dp[i, prev]
    return dfs(0)[1]
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        ans.append(solve(input()))
    print(*ans, sep='\n')