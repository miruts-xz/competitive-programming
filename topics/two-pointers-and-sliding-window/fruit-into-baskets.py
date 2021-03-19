class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        mx = 1
        l = r = 0
        baskets = {}
        while l < n and r < n:
            if baskets.get(tree[r],0):
                baskets[tree[r]] += 1
                r += 1
                mx = max(mx, r-l)
            elif len(baskets) < 2:
                baskets[tree[r]] = 1
                r += 1
                mx = max(mx, r-l)
            else:
                count = baskets.get(tree[l],0)
                if count > 1:
                    baskets[tree[l]] -= 1
                else:
                    del baskets[tree[l]]
                l += 1
        return mx
