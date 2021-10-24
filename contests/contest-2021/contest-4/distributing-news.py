from collections import defaultdict
n, m = map(int, input().split())
groups = []
for _ in range(m):
    groups.append(list(map(int, input().split()))[1:])
class UnionFind:
    def __init__(self, n):
        self.parent, self.size = [i for i in range(n+1)], [1 for _ in range(n+1)]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py], self.size[px] = px, self.size[px]+self.size[py]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
data = UnionFind(n)
for g in groups:
    if not g: continue
    p1 = g[0]
    for p in g[1:]:
        data.union(p1, p)
print(*[data.size[data.find(i)] for i in range(1, n+1)], sep=' ')