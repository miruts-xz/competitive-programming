class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return max(self.getMaxMoney(nums, memo,0), self.getMaxMoney(nums,memo,1))
    def getMaxMoney(self, nums: List[int],memo, i)-> int:
        if not 0 <= i < len(nums):
            return 0
        if memo.get(i, -1) == -1:   
            mx = 0
            for j in range(i+2, len(nums)):
                mx = max(self.getMaxMoney(nums,memo,j), mx)
            memo[i] = mx+nums[i]
        return memo[i]
