class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n - 1
        h = 0
        while l <= r:
            mid = l + (r - l) // 2
            v = citations[mid]
            if v >= n - mid:
                h = max(h, n - mid)
                r = mid - 1
            else:
                h = max(h, v)
                l = mid + 1
        return h
