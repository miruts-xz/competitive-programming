from collections import defaultdict
def fact(n):
    if n < 0:
        return 0
    temp = 1
    res = 1
    while temp <= n:
        res *= temp
        temp += 1
    return temp
def ways(nums)->int:
    topics = defaultdict(int)
    difficulties = defaultdict(int)
    for t, d in nums:
        topics[t] += 1
        difficulties[d] += 1
    t = len(topics)
    d = len(difficulties)
    topic = fact(t)/(fact(t-3)*fact(3))
    difficulty = fact(d)/(fact(d-3)*fact(3))
    return topic+difficulty
if __name__ == '__main__':    
    t = int(input())
    tests = []
    for _ in range(t):
        n = int(input())
        tests.append([list(map(int, input().split())) for _ in range(n)])
    for t in tests:
        print(ways(t))
