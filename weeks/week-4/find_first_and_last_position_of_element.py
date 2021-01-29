from typing import List
from binary_search import binarySearch


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        idx = binarySearch(nums, 0, len(nums) - 1, target)
        if idx != -1:
            minIdx = idx
            while minIdx > 0 and nums[minIdx - 1] == target:
                minIdx -= 1
            maxIdx = idx
            while maxIdx < len(nums) - 1 and nums[maxIdx + 1] == target:
                maxIdx += 1
            return [minIdx, maxIdx]
        return [-1, -1]
