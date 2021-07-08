from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        maxLength = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLength = max(maxLength, dp[i][j])
        return maxLength


if __name__ == "__main__":
    print(Solution().findLength([1, 2, 3, 4, 5], [3, 4, 5, 6]))
