from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
def solve(n, adj, outgoing):
    available = n
    ans = [i for i in range(n+1)]
    queue = [-i for i in range(1, n+1) if not outgoing[i]]
    heapify(queue)
    while queue:
        cur = abs(heappop(queue))
        ans[cur] = available
        available -= 1
        for nbr in adj[cur]:
            outgoing[nbr] -= 1
            if not outgoing[nbr]:
                heappush(queue, -nbr)
    return ans[1:]    
if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = defaultdict(list)
    outgoing = [0]*(n+1)
    for _ in range(m):
        st, dst = map(int, input().split())
        adj[dst].append(st)
        outgoing[st] += 1
    print(*solve(n, adj, outgoing))