# Created by mire on 7/13/21. Copyright 2021, All rights reserved.
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.peak(nums, len(nums), 0, len(nums))

    def peak(self, nums: List[int], n: int, l: int, h: int) -> int:
        mid = l + (h - l) // 2
        if mid == 0:
            if nums[mid + 1] < nums[mid]:
                return mid
            return self.peak(nums, n, mid + 1, h)
        elif mid == n - 1:
            if nums[mid - 1] < nums[mid]:
                return mid
            return self.peak(nums, n, l, mid - 1)
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        return self.peak(nums, n, l, mid - 1) if nums[mid - 1] > nums[mid] else self.peak(nums, n, mid + 1, h)


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
