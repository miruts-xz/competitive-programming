from collections import defaultdict
from string import ascii_lowercase
from itertools import zip_longest
from collections import deque
def solve(n, names):
    adj = defaultdict(list)
    incomming = defaultdict(int)
    for i, cur in enumerate(names[:-1]):
        nxt = names[i+1]
        for st, dst in zip_longest(cur, nxt, fillvalue=""):
            if st == dst: continue
            if dst == '': return -1
            if st == '': break
            adj[st].append(dst)
            incomming[dst] += 1
            break
    queue = deque([c for c in ascii_lowercase if not incomming[c]])
    res = []
    while queue:
        char = queue.popleft()
        res.append(char)
        for nbr in adj[char]:
            incomming[nbr] -= 1
            if not incomming[nbr]:
                queue.append(nbr)
    return res if len(res) == 26 else -1
if __name__ == '__main__':
    n = int(input())
    names = [input() for _ in range(n)]
    res = solve(n, names)
    if res == -1:
        print('Impossible')
    else:
        print(''.join(solve(n, names)))
