from string import ascii_lowercase

def solve(nums):
    ans = [ascii_lowercase[:nums[0]]]
    start = ['a']*200
    ans = [start]
    for i in range(1, len(nums)+1):
        new = ans[-1].copy()
        n = nums[i-1]
        if new[n] == 'a':
            new[n] = 'z'
        else:
            new[n] = 'a'
        ans.append(new)
    return [''.join(i) for i in ans]

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        ans.append(solve(list(map(int, input().split()))))
    for a in ans:
        print(*a, sep='\n')