
def solve(n, k, adj, friends, incomming):
    def bfs(start):
        queue = [(start, -1)]
        while queue:
            temp = []
            reached = False
            for room, parent in queue:
                if room in friends: return False
                if room == 1: reached = True
                for nbr in adj[room]: 
                    if nbr == parent: continue
                    temp.append((nbr, room))
            if reached: return True
            queue = temp
        return False
    for room in range(1, n+1):
        if incomming[room] != 1 or room in friends or room == 1: continue
        if bfs(room): return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        friends = set(map(int, input().split()))
        incomming = [0]*(n+1)
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            incomming[u] += 1
            incomming[v] += 1
        ans.append(solve(n,k, adj, friends, incomming))
    print(*ans, sep='\n')