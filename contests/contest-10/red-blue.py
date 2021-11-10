from functools import lru_cache

def getmax(n,m,reds, blues):

    prefix = [0]
    _max = 0
    for r in reds:
        prefix.append(prefix[-1]+r)
        _max = max(_max, prefix[-1])
    prefix = [0]
    _maxb = 0
    for b in blues:
        prefix.append(prefix[-1]+b)
        _maxb  = max(_maxb, prefix[-1])
    return _max+_maxb

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        reds = list(map(int, input().split()))
        m = int(input())
        blues = list(map(int, input().split()))
        ans.append(getmax(n,m, reds, blues))
    print(*ans, sep='\n')