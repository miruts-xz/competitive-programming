from typing import List
t = int(input())
tests = []
for _ in range(t):
    input()
    n, k = map(int, input().split())
    tests.append([[n, k]]+[list(map(int, input().split())) for _ in range(n-1)])

def gardner(tree: List[List[int]]):
    n, k = tree[0][0], tree[0][1]
    adj_list = [[] for _ in range(n+1)]
    edge_count = [0]*(n+1)
    for i in range(1, len(tree)):
        st, dst = tree[i][0], tree[i][1]
        adj_list[st].append(dst)
        adj_list[dst].append(st)
        edge_count[st] += 1
        edge_count[dst] += 1
    queue = []
    for node in range(1, n+1):
        if edge_count[node] <= 1:
            queue.append(node)
    deleted = 0
    while k and queue:
        deleted += len(queue)
        temp_queue = []
        for node in queue:
            for nbr in adj_list[node]:
                edge_count[nbr] -= 1
                if edge_count[nbr] == 1:
                    temp_queue.append(nbr)
        k -= 1
        queue = temp_queue
    return n-deleted
for t in tests:
    print(gardner(t))
        
    
