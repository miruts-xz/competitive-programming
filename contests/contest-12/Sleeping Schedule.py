from functools import lru_cache
import sys
sys.setrecursionlimit(5000)
def solve(n,h,l,r, times)->int:
    dp = {}
    def dfs(i, time):
        if i == n:
            return 1 if l <= time%h <= r else 0
        if (i,time) not in dp:
            dp[i,time] = (l <= time%h <=r)+max(dfs(i+1, time+times[i]-1), dfs(i+1, time+times[i]))
        return dp[i,time]
    return dfs(0,0) - (1 if l == 0 else 0)
if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    print(solve(n,h,l,r, list(map(int, input().split()))))