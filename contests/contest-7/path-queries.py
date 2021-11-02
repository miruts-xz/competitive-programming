from typing import List


n, m = map(int, input().split())
edges = []
for _ in range(n-1):
    edges.append(list(map(int, input().split())))
queries = list(map(int, input().split()))
def num_pairs(edges, queries)->List[int]:
    adj_list = [[] for _ in range(len(edges)+2)]
    # print(edges)
    for st, dst, w in edges:
        print(st, dst)
        adj_list[st].append([dst, w])
        adj_list[dst].append([st, w])
    dp = {}
    res = []
    visited = set()
    def dfs(node, q)->int:
        if (node, q) in dp:
            return dp[(node, q)]
        total = 1
        for nbr, w in adj_list[node]:
            if w <= q and nbr not in visited:
                visited.add(nbr)
                total += dfs(nbr, q)
                visited.remove(nbr)
        dp[(node, q)] = total+1
        return total+1
    for q in queries:
        visited.clear()
        dp.clear()
        res.append(dfs(1, q))
    return res
print(*num_pairs(edges, queries),sep=' ')
