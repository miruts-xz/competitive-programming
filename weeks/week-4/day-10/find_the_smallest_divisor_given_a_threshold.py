import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = 1000000
        result = r
        while l <= r:
            mid = l + (r - l) // 2
            if self.sumDivision(nums, mid, threshold) <= threshold:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        return result

    def sumDivision(self, nums: List[int], d, t: int):
        s = 0
        for n in nums:
            s += math.ceil(n / d)
            if s > t:
                return s
        return s
