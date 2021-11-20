from math import comb
import bisect
def solve(n, teachers, students):
    sdiff = [teachers[i]-students[i] for i in range(n)]
    sdiff.sort()
    count = 0
    for i,num in enumerate(sdiff):
        lookfor = 1-num
        count += (n-bisect.bisect_left(sdiff, lookfor, i+1, n))
    return count
if __name__ == '__main__':
    n = int(input())
    teachers = list(map(int, input().split()))
    students = list(map(int, input().split()))
    print(solve(n, teachers, students))