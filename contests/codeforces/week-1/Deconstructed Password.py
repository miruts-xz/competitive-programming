
from string import ascii_lowercase
def solve(n, password):
    ans = [None]*(n+1)
    visited = set()
    index = 0
    for i, num in enumerate(password, 1):
        if num <= i: return '-1'
        if num == n+1:
            if not ans[i]: 
                if ascii_lowercase[index%26] in visited or index == 26: return '-1'
                ans[i] = ascii_lowercase[index%26]
                visited.add(ascii_lowercase[index%26])
                index += 1
            else:
                visited.add(ans[i])
            continue
        if num > n+1 or ans[num]: return '-1'
        if ans[i]: 
            if ans[i] in visited: return '-1'
            ans[num] = ans[i]
        else:
            if index == 26: return '-1'
            ans[i] = ascii_lowercase[index%26]
            ans[num] = ans[i]
            index += 1

    return ''.join(ans[1:])


if __name__ == '__main__':
    n = int(input())
    print(solve(n, map(int, input().split())))