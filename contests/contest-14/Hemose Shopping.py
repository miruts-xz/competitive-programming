def solve(n,x,nums):
    srt = sorted(nums)
    if srt == nums: return 'YES'
    if x >= n:
        return 'NO'
    if n >= 2*x or nums[n-x:x]==srt[n-x: x]:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, x = map(int, input().split())
        nums = list(map(int, input().split()))
        ans.append(solve(n,x,nums))
    print(*ans, sep='\n')