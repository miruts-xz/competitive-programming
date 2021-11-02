from math import comb
n, m, t = map(int, input().split())

print(comb(n, 4)*m*comb(n+m-5, t-5))
