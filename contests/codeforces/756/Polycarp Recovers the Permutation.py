from collections import deque
def solve(n, nums):
    ans = deque()
    maxx = max(nums)
    if maxx != nums[0] and maxx != nums[-1]: return [-1]
    l, r = 0, n-1
    while l <= r:
        if nums[l] < nums[r]:
            ans.appendleft(nums[l])
            l += 1
        else:
            ans.append(nums[r])
            r -= 1
    return list(ans)

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        ans.append(solve(n, list(map(int, input().split()))))
    for a in ans:
        print(*a)