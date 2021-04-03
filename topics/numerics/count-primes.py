class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        primes = [True]*(n)
        primes[0] = False
        primes[1] = False
        m = int(math.sqrt(n))
        for i in range(2, m+1, 1):
            if primes[i]:
                for k in range(i*i, n, i):
                    primes[k] = False
        return primes.count(True)
