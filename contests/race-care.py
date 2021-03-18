class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        v = set()
        q.append((1, 2, 1))
        q.append((0, -1, 1))
        v.add((1,2))
        v.add((0,-1))
        while q:
            p, s, l = q.popleft()
            if p == target:
                return l
            if p < 0 or p > 2*target:
                continue
            if (p+s, s*2) not in v:
                v.add((p+s, s*2))
                q.append((p+s, s*2, l+1))
            if (p, -1 if s > 0 else 1) not in v:
                v.add((p, -1 if s > 0 else 1))
                q.append((p, -1 if s > 0 else 1, l+1))
