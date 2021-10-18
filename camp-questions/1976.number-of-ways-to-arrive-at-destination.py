#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        wel = [[] for _ in range(n)]
        for st, dst, w in roads:
            wel[st].append((dst,w))
        def dfs(i)->int:
            if i == n-1:
                return 0
            return min([w+dfs(nh) for nh, w in wel[i]]+[inf])
        minimum = dfs(0)
        ways = 0
        visited = set()
        def getCount(i,total)->int:
            nonlocal ways
            if total < 0:
                return 
            if i == n-1 and total == 0:
                ways += 1
            for nh, w in wel[i]:
                if nh not in visited:
                    visited.add(nh)
                    getCount(nh, total-w)
                    visited.remove(nh)
        visited.add(0)
        getCount(0,minimum)
        return ways
# @lc code=end

