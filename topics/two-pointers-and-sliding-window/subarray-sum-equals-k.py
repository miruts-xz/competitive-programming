class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        r_sums = {0: 1}
        count = prev_sum = 0
        for n in nums:
            new_sum = prev_sum + n
            if r_sums.get(new_sum-k,0):
                count += r_sums.get(new_sum-k)
            r_sums[new_sum] = r_sums.get(new_sum,0) + 1
            prev_sum = new_sum
        return count
