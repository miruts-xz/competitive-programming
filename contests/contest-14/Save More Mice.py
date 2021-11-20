

def solve(n, k, locs):
    total = 0
    count = 0
    i = 0
    while i < k and locs[i] > total:
        count += 1
        total += n-locs[i]
        i += 1
    return count


if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans.append(solve(n,k, sorted(list(map(int, input().split())), reverse=True)))
    print(*ans, sep='\n')