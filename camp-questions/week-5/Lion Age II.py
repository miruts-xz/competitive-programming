from collections import defaultdict
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
def solve(name, k, n, adj,edge_weights):
    size = len(name)
    @lru_cache(maxsize=None)
    def dfs(i,left, prev=None):
        if i == size or left == 0:
            if i < size:
                if (prev, name[i]) in edge_weights:
                    ans = edge_weights[prev, name[i]] + dfs(i+1, left, name[i])
                    return ans
                return dfs(i+1, left, name[i])
            return 0
        if not prev:
            max_start = -float('inf')
            skip = dfs(i+1, left, name[i])
            for high in adj:
                max_start = max(max_start, dfs(i+1, left-1, high))
            return max(skip, max_start)
        skip_score = 0
        if (prev, name[i]) in edge_weights:
            skip_score = edge_weights[prev, name[i]]
        skip_score += dfs(i+1, left, name[i])
        # reset score
        max_reset = -float('inf')
        for high in adj:
            reset_score = -float('inf')
            if (prev, high) in edge_weights:
                reset_score = edge_weights[prev, high]
            reset_score = (reset_score if reset_score != -float('inf') else 0) + dfs(i+1, left-1, high)
            max_reset = max(reset_score, max_reset)
        continue_score = -float('inf')
        if prev in adj:
            for nbr in adj[prev]:
                continue_score = max(continue_score, edge_weights[prev, nbr]+dfs(i+1, left-1,nbr))
        return max(skip_score, max_reset, continue_score)
    return dfs(0,k)

if __name__ == '__main__':
    name, k = input().split()
    n = int(input())
    edges = []
    for _ in range(n):
        edges.append(input().split())
    
    adj = defaultdict(list)
    edge_weights = defaultdict(int)
    for st, dst, w in edges:
        adj[st].append(dst)
        edge_weights[(st, dst)] = int(w)
    print(solve(name, int(k), n, adj,edge_weights))

