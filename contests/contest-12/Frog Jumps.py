
def solve(jumps):
    n = len(jumps)
    l, r = 0, 1
    _max = 1
    while r < n:
        if jumps[r] == 'R':
            _max = max(_max, r-l)
            l = r
        r += 1
    return max(_max, r-l)
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve('R'+input()+'R'))
    print(*ans, sep='\n')