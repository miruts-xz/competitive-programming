def solve(n, nums):
    
    l, r = 0, 1
    _max = 1
    while r < n:
        if nums[r] <= nums[r-1]:
            _max = max(_max, r-l)
            l = r
        r += 1
    return max(_max, r-l)

if __name__ == '__main__':
    n = int(input())
    print(solve(n, list(map(int, input().split()))))