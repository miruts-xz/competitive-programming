

def solve(n, nums):
    i = 1
    res = [0, 0, 0]
    state = 0
    while i < n:
        if state == 0 and nums[i] < nums[res[state]]:
            res[state] = i
        elif state == 1 and nums[i] > nums[res[state]]:
            res[state] = i
        elif state == 0 and nums[i] > nums[res[state]]:
            state += 1
            res[state] = i
        elif state == 1 and nums[i] < nums[res[state]]:
            state += 1
            res[state] = i
        elif state == 2:
            break
        i += 1
    res = [i+1 for i in res]
    return res if res[2] != 1 else -1

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        ans.append(solve(n, list(map(int,input().split()))))
    for a in ans:
        if a != -1:
            print('YES')
            print(*a)
        else:
            print('NO')