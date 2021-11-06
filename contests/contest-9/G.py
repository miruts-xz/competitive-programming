from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from functools import lru_cache

def solve(n, min_maxes, edges):
    values = [0]*(n+1)
    adj = [[] for _ in range(n+1)]
    for st, dst in edges:
        adj[st].append(dst)
        adj[dst].append(st)
    starts = [i for i in range(1, n+1) if len(adj[i]) < 2]
    values[starts[0]] = min_maxes[starts[0]][0]
    def dfs(node, parent=-1)->int:
        my_value = values[node]
        total = 0
        for nbr in adj[node]:
            if nbr == parent: continue
            ifmin, ifmax = abs(min_maxes[nbr][0]-my_value), abs(min_maxes[nbr][1]-my_value)
            if ifmin > ifmax:
                total += abs(min_maxes[nbr][0]-my_value)
                values[nbr] = min_maxes[nbr][0]
            else:
                total += abs(min_maxes[nbr][1]-my_value)
                values[nbr] = min_maxes[nbr][1]
            total += dfs(nbr, node)
        return total
    max_beauty = 0
    for i in [0, 1]:
        values[starts[0]] = min_maxes[starts[0]][i]
        max_beauty = max(max_beauty, dfs(starts[0]))
    return max_beauty

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        min_maxes = [[]]
        edges = []
        for _ in range(n):
            min_maxes.append(list(map(int, input().split())))
        for _ in range(n-1):
            edges.append(list(map(int, input().split())))
        ans.append(solve(n, min_maxes, edges))
    print(*ans, sep='\n')