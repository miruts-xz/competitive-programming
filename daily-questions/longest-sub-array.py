from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        res = 1
        left = 0
        for right in range(len(nums)):
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            max_queue.append(nums[right])
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            min_queue.append(nums[right])
            while left <= right and min_queue and max_queue and max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().longestSubarray(
        [7, 40, 10, 10, 40, 39, 96, 21, 54, 73, 33, 17, 2, 72, 5, 76, 28, 73, 59, 22, 100, 91, 80, 66, 5, 49, 26, 45,
         13, 27, 74, 87, 56, 76, 25, 64, 14, 86, 50, 38, 65, 64, 3, 42, 79, 52, 37, 3, 21, 26, 42, 73, 18, 44, 55, 28,
         35, 87], 63))
