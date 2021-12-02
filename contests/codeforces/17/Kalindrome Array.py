import sys
sys.setrecursionlimit(200001)
def solve(nums, l, r, remove=None):
    while l < r:
        if nums[l] != nums[r]:
            if not remove:
                return solve(nums, l+1, r, nums[l]) or solve(nums, l, r-1, nums[r])
            if remove == nums[l]: return solve(nums, l+1, r, remove)
            if remove == nums[r]: return solve(nums, l, r-1, remove)
            return False
        l += 1
        r -= 1
    return True
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        ans.append('YES' if solve(nums, 0, n-1) else 'NO')
    print(*ans, sep='\n')