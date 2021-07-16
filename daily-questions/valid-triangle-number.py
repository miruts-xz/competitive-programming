# Created by mire on 7/16/21. Copyright 2021, All rights reserved.
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            x = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    continue
                while x < len(nums) and nums[i] + nums[j] > nums[x]:
                    x += 1
                    count += x - j - 1
        return count


if __name__ == "__main__":
    print(Solution().triangleNumber([1, 2, 3, 4, 5, 2]))
