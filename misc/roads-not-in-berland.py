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
cycles = []
edges = []
for _ in range(int(input())-1):
    edges.append(list(map(int, input().split())))
data = UnionFind(len(edges)+1)
for st, dst in edges:
    cycles.append([st, dst]) if data.find(st) == data.find(dst) else data.union(st, dst)
ans = []
cycle = 0
for nbr in range(1, len(edges)+2):
    if data.find(1) != data.find(nbr):
        ans.append([*cycles[cycle], 1, nbr])
        data.union(1, nbr)
        cycle += 1
print(len(ans))
for i, j, u, v in ans:
    print(i, j, u, v, sep=' ')