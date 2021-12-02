
def solve(n, l, r, k, chocolates):
    chocolates.sort()
    count = 0
    for c in chocolates:
        if c > r or k < c: break
        if c >= l: count += 1; k -= c
    return count

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, l, r, k = map(int, input().split())
        chocolates = list(map(int, input().split()))
        ans.append(solve(n,l,r,k, chocolates))
    print(*ans,sep='\n')