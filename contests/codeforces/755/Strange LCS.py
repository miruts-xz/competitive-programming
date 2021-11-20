from collections import defaultdict
from functools import lru_cache, reduce
def solve(words):
    subsequences = {}

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input())
        ans.append(solve(words))
    for a in ans:
        print(*a, sep='\n')

        '''
        "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
        "aaaba"
        '''