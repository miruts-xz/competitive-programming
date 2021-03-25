class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_edges_adj = [[] for i in range(n)]
        blue_edges_adj = [[] for j in range(n)]
        for s, e in red_edges:
            red_edges_adj[s].append(e)
        for s,e in blue_edges:
            blue_edges_adj[s].append(e)
        res = [-1 for i in range(n)]
        res[0] = 0
        for i in range(1, n):
            visited = set()
            dist = self.bfs(red_edges_adj, blue_edges_adj,visited,i)
            res[i] = -1 if dist >= sys.maxsize else dist
        return res
    
    def bfs(self, red_edges: List[List[int]], blue_edges: List[List[int]], visited: set(), target: int)->int:
        q = deque()
        for n in red_edges[0]:
            q.append((0, n, 1, 1))
        for n in blue_edges[0]:
            q.append((0, n, 1, 0))
        while q:
            fr, to, l,flag = q.popleft()
            if to == target:
                return l
            if flag == 0:
                for n in red_edges[to]:
                    if (to,n,flag^1) not in visited:
                        visited.add((to,n,flag^1))
                        q.append((to,n,l+1,flag^1))
            if flag == 1:
                for n in blue_edges[to]:
                    if ((to,n,flag^1)) not in visited:
                        visited.add((to,n,flag^1))
                        q.append((to,n, l+1, flag^1))
        return sys.maxsize
