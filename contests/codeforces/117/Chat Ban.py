from math   import sqrt, floor
from fractions import Fraction
def solve(k, y):
    if (k**2+k)//2 >= y:
        numerator = -1+ sqrt(1+8*y)
        res = Fraction(numerator)//2 + (1 if numerator%2 else 0)
        return res
    elif k**2 <= y:
        return 2*k-1
    else:
        res = 2*k
        numerator = -1 + sqrt(1+8*(k**2-y))
        left = floor(Fraction(numerator)//2)
        res -= left+1
        return res

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    print(*ans, sep='\n')