# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n
        bad = r
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                bad = min(bad, mid)
                r = mid - 1
            else:
                l = mid + 1
        return bad
