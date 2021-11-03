from math import comb, factorial as fact
n = int(input())
# unique = fact(n-1)
# comb(n/2-1)
print(comb(n, n//2)//2*fact(n//2-1)*fact(n//2-1))
