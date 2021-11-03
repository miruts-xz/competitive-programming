from collections import defaultdict, deque
t = int(input())
tests = []
for _ in range(t):
    input()
    nums = list(input().split())
    colors = [c for c in input()]
    tests.append([nums, colors])
def can_permute(nums, colors)->str:
    n = len(nums)
    blues = defaultdict(int)
    red = defaultdict(int)
    # print(nums)
    for i in range(len(nums)):
        num = nums[i]
        color = colors[i]
        if color == "B":
            blues[num] += 1
        else:
            red[num] += 1
    for i, num in enumerate(nums):
        if int(num) > n and colors[i] != 'B':
            return 'NO'
        elif abs(blues[num]-red[num]) > 2:
            return 'NO'
    return 'YES'

for t in tests:
    print(can_permute(t[0], t[1]))