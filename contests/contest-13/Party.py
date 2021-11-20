
def solve(n,m,assigns, prices):
    pptr = 0
    cost = 0
    for a in assigns:
        if pptr < a:
            cost += prices[pptr]
            pptr += 1
        else:
            cost += prices[a-1]
    return cost
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        assigns = sorted(list(map(int, input().split())), reverse=True)
        prices = list(map(int, input().split()))
        ans.append(solve(n,m,assigns, prices))
    print(*ans, sep='\n')