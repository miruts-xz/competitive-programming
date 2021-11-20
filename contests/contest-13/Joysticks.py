
def solve(a1, a2):
    if a1 > a2:
        a1, a2 = a2, a1
    if a1 <= 0:
        return 0
    return 1 + solve(a1+1, a2-2)


if __name__ == '__main__':
    a1, a2 = map(int, input().split())
    if a1 < 2 and a2 < 2:
        print(0)
    else:
        print(solve(a1, a2))
