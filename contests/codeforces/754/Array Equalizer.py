
def solve(n,a,b,query):
    needed = [a[i]-b[i] for i in range(n)]
    incs, decs = 0, 0
    count = 0
    for i in range(1,n):
        if needed[i] < 0: decs += -needed[i]
        if needed[i] > 0: incs += needed[i]
        count += abs(needed[i])
        for j in range(i, n, i):
            needed[j] += needed[i]
    needed1 = a[0]-query
    if needed1 < 0:
        count -= min(abs(decs), abs(needed1-decs))
    if needed1 > 0:
        count -= min(abs(incs), abs(needed1-incs))
    return count+needed1
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    ans = []
    for _ in range(q):
        ans.append(solve(n,a,b,int(input())))
    print(*ans, sep='\n')