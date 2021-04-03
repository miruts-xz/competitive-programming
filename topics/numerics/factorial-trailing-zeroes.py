class Solution:
    def trailingZeroes(self, n: int) -> int:
        if not n:
            return n
        c = 0
        for i in range(1,int(math.log(n,5))+1):
            c += n // 5**i
        return c
