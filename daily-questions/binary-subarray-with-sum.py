# Created by mire on 7/11/21. Copyright 2021, All rights reserved.
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = [0] * (len(nums) + 1)
        res = s = 0
        counts[0] = 1
        for n in nums:
            s += n
            if s >= goal:
                res += counts[s - goal]
            counts[s] += 1
        return res


if __name__ == '__main__':
    print(Solution().numSubarraysWithSum([0, 1, 0, 0, 1, 1, 0, 1], 2))
