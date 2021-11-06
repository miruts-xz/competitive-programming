#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        reverse_prefix = [0]*(n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i]+num
        for i in range(n-1, -1, -1):
            reverse_prefix[i] = reverse_prefix[i+1]+nums[i]
        print("Prefix", prefix, reverse_prefix, sep='\n')
        largest = 0
        
        firstLen_run = [0]*(n+1)
        secondLen_run = [0]*(n+1)
        firstLen_run[firstLen-1] = prefix[firstLen]
        secondLen_run[secondLen-1] = prefix[secondLen]
        for j in range(firstLen+1, n+1):
            firstLen_run[j] = max(firstLen_run[j-1], prefix[j]-prefix[j-firstLen])
        for j in range(secondLen+1, n+1):
            secondLen_run[j] = max(secondLen_run[j-1], prefix[j]-prefix[j-secondLen])
        # print("Running Sum", firstLen_run, secondLen_run, sep='\n')
        max_rev = 0
        for j in range(n-firstLen,0,-1):
            max_rev = max(max_rev, reverse_prefix[j]-reverse_prefix[j+firstLen])
            largest = max(largest, secondLen_run[j-1]+max_rev)
        max_rev = 0
        for j in range(n-secondLen, 0, -1):
            max_rev = max(max_rev, reverse_prefix[j]-reverse_prefix[j+secondLen])
            largest = max(largest, firstLen_run[j-1]+max_rev)
        return largest
# @lc code=end

