from math import comb
from itertools import combinations, permutations, repeat
n, k = map(int, input().split())

total_maches = comb(n, 2)
if n*k > total_maches:
    print('-1')
else:
    print(k*n)
    # print(comb(n, 2))
    visited = set()
    wons = [0 for _ in range(n+1)]
    for winner, losser in permutations(range(1, n+1), 2):
        if wons[winner] == k or (winner, losser) in visited or (losser, winner) in visited: continue
        visited.add((winner, losser))
        wons[winner] += 1
        print(winner, losser, sep=' ')
