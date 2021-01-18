class Solution:
    def tribonacci(self, n: int) -> int:
        prev0, prev1, prev2 = 1, 1, 0
        if n == 0:
            return 0
        if n <= 2:
            return 1
        while n > 2:
            prev0, prev1, prev2 = prev0 + prev1 + prev2, prev0, prev1
            n -= 1
        return prev0
