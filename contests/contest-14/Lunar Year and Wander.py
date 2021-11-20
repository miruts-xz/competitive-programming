from heapq import heappush, heappop
def solve(n, m, adj):
    ans = []
    queue = [1]
    visited = set([1])
    while queue:
        cur = heappop(queue)
        ans.append(cur)
        for nbr in adj[cur]:
            if nbr in visited:continue
            visited.add(nbr)
            heappush(queue, nbr)
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        st, dst = map(int, input().split())
        adj[st].append(dst)
        adj[dst].append(st)
    print(*solve(n, m, adj))
