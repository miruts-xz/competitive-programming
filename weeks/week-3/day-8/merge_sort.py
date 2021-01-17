from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.temp = [0] * n
        self.mergeSort(nums, 0, n - 1)
        return nums

    def mergeSort(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.mergeSort(nums, lo, mid)
        self.mergeSort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums: List[int], left, mid, right):
        i, j = left, mid + 1
        for k in range(left, right + 1):
            self.temp[k] = nums[k]
        for k in range(left, right + 1):
            if i > mid:
                nums[k] = self.temp[j]
                j += 1
            elif j > right:
                nums[k] = self.temp[i]
                i += 1
            elif self.temp[i] <= self.temp[j]:
                nums[k] = self.temp[i]
                i += 1
            else:
                nums[k] = self.temp[j]
                j += 1
