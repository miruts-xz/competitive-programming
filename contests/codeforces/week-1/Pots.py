from collections import Counter
def solve(n, nums):
    return Counter(nums).most_common()[0][1]


if __name__ == '__main__':
    n = int(input())
    print(solve(n, list(map(int, input().split()))))