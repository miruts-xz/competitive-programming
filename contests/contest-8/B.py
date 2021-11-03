from collections import defaultdict, deque
def repost_length(reposts)->int:
    n = len(reposts)
    adj = defaultdict(list)
    for sharer, _, poster in reposts:
        adj[poster].append(sharer)
    q = deque([('polycarp',1)])
    visited = set()
    longest = 1
    while q:
        cur, shares = q.popleft()
        longest = shares
        for nbr in adj[cur]:
            if nbr in visited: continue
            visited.add(nbr)
            q.append((nbr, shares+1))
    return longest
if __name__ == '__main__':
    reposts = [list(map(str.lower, input().split())) for _ in range(int(input()))]
    print(repost_length(reposts))