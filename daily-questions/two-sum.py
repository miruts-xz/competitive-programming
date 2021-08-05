from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            idx = d.get(target - n, None)
            if idx is not None:
                return [idx, i]
            d[n] = i


if __name__ == "__main__":
    print(Solution().twoSum([1, 2, 3, 4, 5], 6))
