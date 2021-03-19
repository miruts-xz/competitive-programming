class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = rsum = 0
        for n in nums:
            total += n
        for i in range(len(nums)):
            rsum += nums[i]
            if rsum == total:
                return i
            total -= nums[i]
        return -1
