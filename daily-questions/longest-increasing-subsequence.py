from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        mx = 1
        for i in range(len(nums)):
            if not memo.get(i, None):
                mx = max(mx, self.getLength(nums, i, memo))
        return mx

    def getLength(self, nums: List[int], st, memo) -> int:
        if st == len(nums) - 1:
            return 1
        if memo.get(st, None):
            return memo[st]
        mx = 1
        for i in range(st + 1, len(nums)):
            if nums[i] > nums[st]:
                mx = max(mx, self.getLength(nums, i, memo) + 1)

        memo[st] = mx
        return mx


if __name__ == "__main__":
    print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
