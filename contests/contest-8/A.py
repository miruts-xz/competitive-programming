from collections import deque
def can_go(n, nums, t)->str:
    adj_list = [[] for _ in range(n+1)]
    for i, num in enumerate(nums):
        st, dst = i+1, num+i+1
        adj_list[st].append(dst)
    q = deque([1])
    visited = [False for _ in range(n+1)]
    while q:
        cur = q.popleft()
        if cur == t:
            return 'YES'
        for nbr in adj_list[cur]:
            if visited[nbr]: continue
            visited[nbr] = True
            q.append(nbr)
    return 'NO'
if __name__ == '__main__':
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))
    print(can_go(n, nums, t))