
class UnionFind:
    def __init__(self, n):
        self.parent, self.size = [i for i in range(n+1)], [1 for _ in range(n+1)]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: 
            self.size[px] += 1
            return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py], self.size[px] = px, self.size[px]+self.size[py]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def solve(n, d, edges):
    print(edges)
    uf = UnionFind(n)
    ans = []
    for st, dst in edges:
        uf.union(st, dst)
        ans.append(max(uf.size)-1)
    return ans

if __name__ == '__main__':
    ans = []
    n, d = map(int, input().split())
    edges = []
    for _ in range(d):
        edges.append(list(map(int, input().split())))
    ans = solve(n, d, edges)
    print(*ans, sep = '\n')