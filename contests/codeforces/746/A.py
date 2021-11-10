from math import ceil
def min_times(H, weapons):
    weapons.sort()
    large1, large2 = weapons[-1], weapons[-2]
    if large1 >= H:
        return 1
    ceil([2,3,4])
    count = 2*(H//(large1+large2))
    rem = H%(large1+large2)
    if rem == 0:
        return count
    elif rem > large1:
        count += 2
    else:
        count += 1
    return count
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, H = map(int, input().split())
        ans.append(min_times(H, list(map(int, input().split()))))
    print(*ans, sep='\n')