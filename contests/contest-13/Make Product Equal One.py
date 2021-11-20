from functools import reduce
def solve(n, nums):
    costs = [(num+1) if num < 0 else (num-1) for num in nums]
    smallers = reduce(lambda c, num: (c+1) if num < 0 else c,nums, 0)
    ans = reduce(lambda c, cost: c+abs(cost), costs, 0)
    if smallers%2 and 0 not in nums:
        ans += 2
    return ans


if __name__ == '__main__':
    n = int(input())
    print(solve(n, list(map(int, input().split()))))