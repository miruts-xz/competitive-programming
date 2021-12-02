#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, n = 0,len(nums)
        furthest = i = 0
        dp = [float(inf)]*n
        dp[0] = 0
        for i in range(n-1):
            for j in range(i+1, i+nums[i]+1):
                if j == n: return dp[n-1]
                dp[j] = min(dp[j], dp[i]+1)
        return dp[n-1]

# @lc code=end

