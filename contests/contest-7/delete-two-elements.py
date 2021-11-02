
from collections import defaultdict


def pairs(nums):
    n = len(nums)
    total = sum(nums)
    avg = total/n
    target = total-avg*(n-2)
    occurences = defaultdict(int)
    pair_count = 0
    for i, num in enumerate(nums):
        pair_count += occurences[target-num]
        occurences[num] += 1
    return pair_count
if __name__ == '__main__':
    t = int(input())
    tests = []
    ans = []
    for _ in range(t):
        input()
        ans.append(pairs(list(map(int, input().split()))))
    print(*ans, sep='\n')