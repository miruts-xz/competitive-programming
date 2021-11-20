
def solve(n,k, nums):
    x = 0
    steps = 0
    nums.sort(key=lambda y: (k-(y%k))%k)
    for num in nums:
        rem = num%k
        
    return steps

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans.append(solve(n,k, list(map(int, input().split()))))
    print(*ans, sep='\n')