
from typing import DefaultDict
from collections import Counter, defaultdict
from math import comb
def num_pairs(nums)->int:
    n, l, r = nums[0], nums[1], nums[2]
    nums = nums[3:]
    nums.sort()
    ans =  comb(n, 2)
    inv = 0
    lo, hi = 0, n-1
    while lo < hi:
        ss = nums[lo]+nums[hi]
        if ss < l:
            inv += (hi-lo)
            lo += 1
        else:
            hi -= 1
    lo, hi = 0, n-1
    while lo < hi:
        ss = nums[lo]+nums[hi]
        if ss > r:
            inv += (hi-lo)
            hi -= 1
        else:
            lo += 1
    return comb(n,2)-inv
t = int(input())
tests = []
for _ in range(t):
    n, l, r = map(int, input().split())
    tests.append([n, l, r]+list(map(int, input().split())))
for t in tests:
    print(num_pairs(t))