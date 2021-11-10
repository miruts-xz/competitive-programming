from collections import defaultdict

import sys
sys.setrecursionlimit(5000)
def party():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        employee = int(input())
        graph[employee].append(i + 1)
    def dfs(root):
        if graph[root] is None:
            return 0
        depth = 0
        for child in graph[root]:
            depth = max(depth, 1 + dfs(child))
        return depth
    depth = dfs(-1)
    print(depth)

party()
