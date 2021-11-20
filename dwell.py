from collections import defaultdict
from functools import lru_cache, reduce
def solve(words):
    word1, word2 = None, None
    commons = defaultdict(list)
    @lru_cache(maxsize=None)
    def dfs(i, j, chosei, chosej):
        nonlocal word1, word2
        if i == len(word1) or j == len(word2):
            return ['']
        if word2[j] == word1[i]:
            return [word1[i] + after for after in dfs(i+1, j+1, chosei, chosej)]
        ip = dfs(i+1, j, chosei, chosej)
        jp = dfs(i, j+1, chosei, chosej)
        ijp = dfs(i+1, j+1, chosei, chosej)
        commons[chosei, chosej].extend(ip)
        commons[chosei, chosej].extend(jp)
        commons[chosei, chosej].extend(ijp)
        ip.extend(jp)
        return ip
    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        commons[i, i+1].extend(dfs(0,0, i, i+1))
    # print(commons[0,1])
    all = set(commons[0,1])
    all = all.intersection(*map(set, commons.values()))
    longest = reduce(lambda c, x: x if len(x) > len(c) else c, all, '')
    return [len(longest), longest]
    
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