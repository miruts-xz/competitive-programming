t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    tests.append(list(map(int, input().split())))
def maximal(nums):
    _min1 = min(nums)
    nums.remove(_min1)
    if not nums:
        return _min1
    _max = max(nums)
    _min2 = min(nums)
    if _min1 >= 0:
        return max(_min1, _max-_min1)
    return _min2-_min1
for t in tests:
    print(maximal(t))
    