
def solve(s, t):
    return 'YES' if set(s).intersection(set(t)) else 'NO'

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(input(), input()))
    print(*ans, sep='\n')