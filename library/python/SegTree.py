

class SegTree:
    def __init__(self, n):
        size = 1
        while size < n: size *= 2
        self.size = size
        self.tree = [0]*(size*2)
        
    def _update(self, k: int, v: int, x: int, lo: int, hi: int):
        if hi-lo == 1:
            self.tree[x] = v
            return
        m = lo + (hi-lo)//2
        if k < m:
            self._update(k,v,2*x+1, lo, m)
        else:
            self._update(k,v,2*x+2, m, hi)
        self.tree[x] = self.tree[2*x+1]+self.tree[2*x+2]
            
    def update(self, k: int, v: int):
        self._update(k, v, 0, 0, self.size)

    def _query(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return 0
        if lx >= l and rx <= r: return self.tree[x]
        m = lx + (rx-lx)//2
        s1 = self._query(l, r, 2*x+1, lx, m)
        s2 = self._query(l, r, 2*x+2, m, rx)
        return s1+s2

    def query(self, l, r):
        return self._query(l, r, 0, 0, self.size)

if __name__ == '__main__':
    seg = SegTree(5)
    for i in range(5):
        seg.update(i, i+1)
    print(seg.tree)
    print(seg.query(4, 5))
