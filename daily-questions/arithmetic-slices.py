class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1]-nums[i]
            r = i+1
            while r < len(nums):
                if nums[r]-nums[r-1] != diff:
                    break
                if r - i >= 2:
                    count += 1
                r += 1
        return count
