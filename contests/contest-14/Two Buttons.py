from math import inf
import sys
sys.setrecursionlimit(100000)

def dfs(n, m):
    if m == n:
        return 0
    if m < n:
        return n-m
    if m%2:
        return 2 + dfs(n, (m+1)//2)
    return 1 + dfs(n, m//2)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(dfs(n, m))