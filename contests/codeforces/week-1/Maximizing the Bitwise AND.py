
def solve(n, nums):
    def check_bits(pattern):
        cnt = 0
        for num in nums:
            if pattern&num == pattern: cnt += 1
        return cnt
    result = 0
    for loc in range(31, -1, -1):
        count = check_bits(result|1 << loc)
        if count > 1:
            result |= 1 << loc
    return result

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))