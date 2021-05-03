class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = -sys.maxsize
        max_ending_cur = 0
        for n in nums:
            max_ending_cur += n
            max_so_far = max(max_so_far, max_ending_cur)
            if max_ending_cur < 0:
                max_ending_cur = 0
        mn_so_far = sys.maxsize
        mn_ending_cur = 0
        for n in nums:
            mn_ending_cur += n
            mn_so_far = min(mn_so_far, mn_ending_cur)
            if mn_ending_cur > 0:
                mn_ending_cur = 0
        return max(abs(mn_so_far), max_so_far)
