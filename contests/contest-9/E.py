from heapq import heappop, heappush
from math import inf
def solve(n, k, locs, temps):
    heap = []
    temperatures = [inf for _ in range(n+1)]
    for l, t in zip(locs, temps):
        heappush(heap, (t, l))
        temperatures[l] = t
    while heap:
        temp, index = heappop(heap)
        cur_index = index+1
        while cur_index <= n and temp + cur_index-index < temperatures[cur_index]:
            temperatures[cur_index] = temp+cur_index-index
            cur_index += 1
        cur_index = index - 1
        while cur_index > 0 and index-cur_index + temp < temperatures[cur_index]:
            temperatures[cur_index] = temp+index-cur_index
            cur_index -= 1
    return temperatures[1:]
            

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        locs = list(map(int, input().split()))
        temps = list(map(int, input().split()))
        ans.append(solve(n, k, locs, temps))
    for a in ans:
        print(*a)