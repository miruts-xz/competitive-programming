

class BIT:
    def __init__(self,n: int):
        self.tree = [0]*(n+1)
        self.n = n
    def add(self, k: int, x: int):
        while k <= self.n:
            self.tree[k] += x
            k += k&-k
    def sum(self, k: int):
        s = 0
        while k > 0:
            s += self.tree[k]
            k -= k&-k
        return s
    def range_sum(self, lo: int, hi: int):
        sum = self.sum(hi)
        if lo > 1: sum -= self.sum(lo-1)
        return sum



