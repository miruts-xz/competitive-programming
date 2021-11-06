from math import comb, factorial as fact
n = int(input())
print(comb(n, n//2)//2*fact(n//2-1)*fact(n//2-1))
