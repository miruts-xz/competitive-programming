
def solve(nums):
    total = sum(nums)
    if total%3: return 1
    return 0


if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(list(map(int, input().split()))))
    print(*ans, sep='\n')