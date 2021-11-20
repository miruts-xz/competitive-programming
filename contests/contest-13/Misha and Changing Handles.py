from collections import defaultdict


def solve(queries):
    old_to_new = defaultdict(str)
    new_to_old = defaultdict(str)
    for old, new in queries:
        if old in new_to_old:
            old_to_new[new_to_old[old]] = new
            new_to_old[new] = new_to_old[old]
        else:
            old_to_new[old] = new
            new_to_old[new] = old
    return [[k, v] for k, v in old_to_new.items()]
if __name__ == '__main__':
    queries = []
    for _ in range(int(input())):
        queries.append(input().split())
    ans = solve(queries)
    print(len(ans))
    for a in ans:
        print(*a)