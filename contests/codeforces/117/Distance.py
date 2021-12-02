from math import ceil
from math import floor
def solve(x, y):
    if (x+y)%2: return '-1 -1'
    return f'{ceil(x/2)} {floor(y/2)}'


if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    print(*ans, sep='\n')