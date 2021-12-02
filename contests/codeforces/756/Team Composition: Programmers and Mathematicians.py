from math import comb
def solve(a, b):
    total = (a+b)//4
    total = min(total, a, b)
    return total
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    print(*ans, sep='\n')