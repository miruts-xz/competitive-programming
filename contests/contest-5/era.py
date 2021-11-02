t = int(input())
def min_operations(nums):
    max_diff = 0
    for i, num in enumerate(nums):
        max_diff = max(max_diff, (num - i-1)) if (num > i) else max_diff
    return max_diff
ans = []
for _ in range(t):
    input()
    print(min_operations(list(map(int, input().split()))))