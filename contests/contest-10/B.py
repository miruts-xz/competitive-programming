from heapq import heappop, heappush
from math import ceil
def solve(n):
    nums = [i for i in range(1, n+1)]
    ans = []
    while len(nums) > 1:
        if nums[-1] == nums[-2]:
            nums.pop()
            ans.append([nums[-1], nums[-1]])
        elif (nums[-1]%2 and nums[-2]%2) or (nums[-1]%2==0 and nums[-2]%2==0):
            ans.append([nums[-1], nums[-2]])
            temp = (nums[-1]+nums[-2])//2
            nums.pop(); nums.pop()
            nums.append(temp)
        elif len(nums) > 2:
            ans.append([nums[-1], nums[-3]])
            nums.pop()
            nums[-2] = nums[-1]
        else:
            ans.append([nums[-1], nums[-2]])
            temp = (nums[-1]+nums[-2])//2 + (1 if (nums[-1]+nums[-2])%2 else 0)
            nums.pop(); nums.pop()
            nums.append(temp)
    return nums[-1], ans
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(int(input())))
    for a  in ans:
        print(int(a[0]))
        for sa in a[1]:
            print(*sa)