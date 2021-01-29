from typing import List


def binarySearch(self, nums: List[int], left, right, target) -> int:
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)
        if nums[mid] > target:
            return self.binarySearch(nums, left, mid - 1, target)
    return -1
