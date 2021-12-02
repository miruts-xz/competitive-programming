from math import factorial as fact
from itertools import count, permutations

def solve(x, y, M, K):
    count = 0
    for num in range(2**(x-2), 2**(x+y-1)-1-(2**(y)-1)+1):
        number = 2**(x+y-1)+num
        if bin(number).count('1') != x or bin(number)[2:].count('0') != y: continue
        if number%M >= K:
            count += 1
    return count
        



if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    # with open('zeros.in', 'r') as fn:
    #     q = int(fn.readline())
    #     for _ in range(q):
    #         params = fn.readline()
    #         ans.append(solve(*list(map(int, params.split()))))
    print(*ans, sep='\n')