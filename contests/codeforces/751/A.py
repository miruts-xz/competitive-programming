

def solve(string):
    min_char = min(string)
    a = min_char
    idx = string.index(a)
    b = ''.join([c for i,c in enumerate(string) if i != idx])
    return [a, b]

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(input()))
    for a in ans:
        print(*a)