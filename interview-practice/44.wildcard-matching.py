#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        @lru_cache(maxsize=None)
        def match(i,j):
            if i == m and j == n: return True
            if i == m: return p[j]=='*' and match(i, j+1)
            if j == n: return False
            if s[i] == p[j] or p[j] == '?':
                return match(i+1, j+1)
            elif p[j] == '*':
                return match(i, j+1) or match(i+1, j) or match(i+1, j+1)
            return False
        return match(0,0)
        
# @lc code=end
# @time=18m
