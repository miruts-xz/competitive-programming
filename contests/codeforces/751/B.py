from collections import defaultdict
from functools import reduce
from typing import Counter

def solve(n, nums, q, query):
    state = defaultdict(list)
    max_query = reduce(lambda c, x: max(x[1], c), query, 0)
    steps = 0
    state[steps] = nums
    changing = True
    while steps < max_query and changing:
        counter = Counter(state[steps])
        steps += 1
        state[steps] = [counter[state[steps-1][i]] for i in range(n)]
        if state[steps] == state[steps-1]:
            changing = False
    ans = []
    for index, step in query:
        if step > steps:
            ans.append(state[steps][index-1])
        else:
            ans.append(state[step][index-1])
    return ans
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        q = int(input())
        query = [list(map(int, input().split())) for _ in range(q)]
        ans.append(solve(n, nums, q, query))
    for a in ans:
        print(*a, sep='\n')