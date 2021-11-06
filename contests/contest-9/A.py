from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from functools import lru_cache

def solve(num):
    count = 0
    for n in num[:-1]:
        if int(n):
            count += int(n)+1
    count += int(num[-1])
    return count


if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        ans.append(solve(input()))
    print(*ans, sep='\n')