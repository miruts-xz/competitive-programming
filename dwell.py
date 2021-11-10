from collections import defaultdict
from functools import lru_cache
from math import inf
def solve(n,m,k,adj):
    ans = [[inf]*m for _ in range(n)]
    start = (0, 0)
    dp = {}
    def dfs(i,j,left)->int:
        nonlocal adj, start
        if (i,j) == start and left == 0:
            return 0
        if left <= 0: return inf
        if (i,j,left) not in dp:
            mn = inf
            for ni, nj, wt in adj[i,j]:
                mn = min(wt+dfs(ni,nj,left-1),mn)
            dp[i,j,left] = mn
        return dp[i,j,left]
    for i in range(n):
        for j in range(m):
            mn = inf
            start = (i,j)
            dp.clear()
            for ni, nj, wt in adj[i,j]:
                mn = min(wt+dfs(ni,nj,k-1),mn)
            ans[i][j] = mn if mn != inf else -1
    return ans
if __name__ == '__main__':
    n, m , k = map(int, input().split())
    adj = defaultdict(list)
    for i in range(n):
        for j, weight in enumerate(list(map(int, input().split()))):
            adj[i,j].append([i,j+1,weight])
            adj[i,j+1].append([i,j,weight])
    for i in range(n-1):
        for j, weight in enumerate(list(map(int, input().split()))):
            adj[i, j].append([i+1, j, weight])
            adj[i+1,j].append([i,j,weight])
    ans = solve(n,m,k,adj)
    for i in range(n):
        print(*[ans[i][j] for j in range(m)])