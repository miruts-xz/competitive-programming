from collections import deque
from math import inf
from heapq import heappop, heappush

def minimum_life(n, m, monsters, points, edges)->int:
    adj = [[] for _ in range(n+1)]
    for src, dst in edges:
        adj[src].append(dst)
    queue = [(0, 0, 0, 1)]
    min_so_far = inf
    visited = [False]*(n+1)
    while queue:
        monster, start, life, cave = heappop(queue)
        min_so_far = start
        visited[cave] = True
        for nbr in adj[cave]:
            if visited[nbr]: continue
            if monsters[nbr] >= life:
                start += (monsters[nbr]-life)+1
                life += points[nbr]+abs(monsters[nbr]-life)+1
            else:
                life += points[nbr]
            heappush(queue, (monsters[nbr], start, life, nbr))
    return min_so_far
ans = []
for _ in range(int(input())):
    n,m = map(int, input().split())
    monsters = list(map(int, input().split()))
    points = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    ans.append(minimum_life(n, m, [0,0]+monsters, [0,0]+points, edges))
print(*ans, sep='\n')