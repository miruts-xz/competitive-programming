from typing import final


t = int(input())
tests = []
for _ in range(t):
    tests.append(list(map(int, input().split())))

def final_position(start, n)->int:
    current = start
    for i in range(1, n+1):
        if current%2:
            current += i
        else:
            current -= i
    return current
for t in tests:
    print(final_position(t[0], t[1]))
