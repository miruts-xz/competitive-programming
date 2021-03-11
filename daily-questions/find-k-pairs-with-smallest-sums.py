import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        q = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(q, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
        for _ in range(min(k, len(q))):
            _, r = heapq.heappop(q)
            result.append(r)
        return result
