from collections import Counter, defaultdict
def solve(nums):
    found = set()
    l, r = 0, 0
    count = defaultdict(int)
    while r < len(nums) and len(found) < 3:
        found.add(nums[r])
        count[nums[r]]+= 1
        r += 1
    if len(found) < 3:
        return 0
    min_so_far = r-l
    r -= 1
    while l < len(nums)-1 and r < len(nums):
        while count[nums[l]] > 1 and count['1'] > 0 and count['2'] > 0 and count['3'] > 0:
            count[nums[l]] -= 1
            min_so_far -= 1
            l += 1
        if r < len(nums)-1:
            count[nums[l]] -= 1
            l += 1
            r += 1
            count[nums[r]] += 1
        else:
            break
    return min_so_far if min_so_far > 2 else 0
    



if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(input()))
    print(*ans, sep='\n')