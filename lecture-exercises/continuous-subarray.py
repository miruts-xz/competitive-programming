class Solution:
    def continuous_subarray(self,nums: List[int]) -> int:
      pr_sum = [0]*(len(nums)+1)
      for i in range(1,len(nums)):
        pr_sum[i] = pr_sum[i-1]+nums[i]
       print(pr_sum)
      
      
