n = int(input())
adj_list, respects, root = [[] for _ in range(n+1)], [0]*(n+1), 1
for i in range(1, n+1):
    p, r = map(int, input().split())
    if p == -1:
        root = i; continue
    adj_list[p].append(i)
    respects[i] = r
ans = []
for V in range(1, n+1):
    if V == root: continue
    if respects[V] and all([respects[c] for c in adj_list[V]]):
        ans.append(V)
print(*ans, sep=' ') if ans else print('-1')


