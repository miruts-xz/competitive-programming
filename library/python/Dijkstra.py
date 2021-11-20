from heapq import heappop, heappush

class Dijkstra:
    def __init__(self, n, adj):
        self.n = n; self.adj = adj
    def shortest_path(self, start):
        self.distance = [float('inf')]*(self.n+1)
        # self.parent = [None]*(self.n+1)
        self.visited = [False]*(self.n+1)
        self.distance[start] = 0
        queue = [(0, start)]
        while queue:
            dist, node = heappop(queue)
            if self.visited[node]: continue
            self.visited[node] = True
            for nbr, weight in self.adj[node]:
                if self.distance[nbr] <= dist+weight: continue
                # self.parent[nbr] = node
                self.distance[nbr] = dist+weight
                heappush(queue, (self.distance[nbr], nbr))



        

