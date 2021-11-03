from typing import Counter


from math import comb
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = Counter(nums)

included = Counter(nums[:3])
ans = 1
for num in included.keys():
    ans *= comb(count[num], included[num])
print(ans)