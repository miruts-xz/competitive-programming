
def solve(n, str1, str2):
    pairs = set()
    _from = set()
    to = set()
    for c1, c2 in zip(str1, str2):
        if c2 in _from and c1 in to or c2 in to and c1 in _from: continue
        
    return list(pairs)

            
        



if __name__ == '__main__':
    ans = solve(int(input()), input(), input())
    print(len(ans))
    for a in ans:
        print(*a)