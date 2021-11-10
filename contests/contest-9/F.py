from itertools import permutations
print(permutations('23',2))
def solve(bosses):
    n = len(bosses)
    count = bosses[0]
    prefix = [0]*n
    for i in range(1, n):
        prefix[i] = prefix[i-1]+bosses[i]
    l, r = 0, 3
    while r < len(prefix):
        if prefix[r]-prefix[l] == 3:
            count += 1
            l, r = r-1, r + 2
        l, r = l+1, r+1
    return count

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        ans.append(solve(list(map(int, input().split()))))
    print(*ans, sep='\n')