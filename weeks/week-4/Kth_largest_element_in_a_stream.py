import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums
        if k < len(nums):
            self.nums = nums[len(nums) - k:]

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]
