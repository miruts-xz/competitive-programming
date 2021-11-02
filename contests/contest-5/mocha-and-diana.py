n, m1, m2 = map(int, input().split())
mocha_edges = []
diana_edges = []
for _ in range(m1):
    mocha_edges.append(list(map(int, input().split())))
for _ in range(m2):
    diana_edges.append(list(map(int, input().split())))
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
mocha_data = UnionFind(n+1)
diana_data = UnionFind(n+1)

for st, dst in mocha_edges:
    mocha_data.union(st, dst)
for st, dst in diana_edges:
    diana_data.union(st, dst)
res = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if mocha_data.find(i) != mocha_data.find(j) and diana_data.find(i) != diana_data.find(j):
            res.append([i, j])
            mocha_data.union(i,j)
            diana_data.union(i,j)
print(len(res))
for pair in res:
    print(*pair)

