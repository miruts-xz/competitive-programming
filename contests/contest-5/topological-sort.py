from functools import cmp_to_key
from heapq import heappop, heappush, heapify
t = int(input())
removes = []
for _ in range(t):
    n, m = map(int, input().split())
    removes.append([[n, m]]+[list(map(int, input().split())) for _ in range(m)])

def topology(removes):
    n, m = removes[0][0], removes[0][1]
    removed = [0]*(n+1)
    for ii in range(1, m+1):
        _, dst = removes[ii]
        removed[dst] += 1
    ans = []
    frontier = [-i for i in range(1, n+1) if removed[i]==i-1]
    heapify(frontier)
    while frontier:
        cur = abs(heappop(frontier))
        ans.append(cur)
        for nbr in range(cur+1, n+1):
            removed[nbr] += 1
            if removed[nbr] == nbr-1:
                heappush(frontier, -nbr)
    return ans
for remove in removes:
    print(*topology(remove), sep=" ")


    