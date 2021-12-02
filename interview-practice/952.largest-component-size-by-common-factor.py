#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent, self.size = [i for i in range(n+1)], [1 for _ in range(n+1)]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        self.parent[px], self.size[py] = py, self.size[py]+self.size[px]
    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return x
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)
        uf = UnionFind(max(nums))
        for i, n in enumerate(nums):
            for m in nums[i+1:]:
                if gcd(m, n) > 1: 
                    uf.union(n, m)
        return max(uf.size)
# @lc code=end
# @time=35m

