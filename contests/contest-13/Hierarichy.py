def solve(n,edges):
    adj = [[] for _ in range(n+1)]
    incomming = [0]*(n+1)
    for su, sb, c in edges:
        adj[sb].append([su, c])
        incomming[sb] += 1
    start = [i for i in range(1, n+1) if not incomming[i]]
    if len(start) > 1: return -1
    start = start[0]
    total = 0
    for i in range(1, n+1):
        if i == start: continue
        total += min([c for su, c in adj[i]])
    return total
if __name__ == '__main__':
    n = int(input())
    qualifications = list(map(int, input().split()))
    edges = []
    for _ in range(int(input())):
        edges.append(list(map(int, input().split())))
    print(solve(n, edges))