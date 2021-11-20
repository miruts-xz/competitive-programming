
def solve(ballons):
    count = 0
    while sum(ballons) > 3 and ballons.count(0) < 2:
        ballons.sort()
        take = min(ballons[-1]//2, ballons[0] if ballons[0] else ballons[1])
        ballons[-1]  -= take*2
        if ballons[0]:
            ballons[0] -= take
        else:
            ballons[1] -= take
        count += take
    if sum(ballons) >= 3 and ballons.count(0) < 2:
        count += 1
    return count

if __name__ == '__main__':
    ballons = list(map(int, input().split()))
    print(solve(ballons))