

def solve(n, nums):
    nums.sort()
    res222 = []
    r = n-1
    while len(res222) < n//2:
        res222.append([nums[r], nums[0]])
        r -= 1
    return res222

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        ans.append(solve(n, list(map(int, input().split()))))
    for a in ans:
        for p in a:
            print(*p)