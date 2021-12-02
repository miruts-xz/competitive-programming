#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(i, nums, results):
            if i == len(nums)-1:
                results.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums = nums[:i]+sorted(nums[i:])
                if j > i and nums[j-1] == nums[j]: continue
                nums[i], nums[j] = nums[j], nums[i]
                permute(i+1, nums, results)
                nums[i], nums[j] = nums[j], nums[i]
        ans = list()
        nums.sort()
        permute(0, nums, ans)
        return ans
        
# @lc code=end
# @time=35m

