
def solve(nums):
    hasEven = False
    for n in nums:
        if n%2 == 0: 
            hasEven = True; break
    if not hasEven: return '-1'
    if nums[-1]%2==0: return '0'
    if nums[0]%2==0: return '1'
    return '2'

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve([int(c) for c in input()]))
    print(*ans, sep='\n')