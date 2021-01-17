#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def getLimit(arr, d):
    count = 0
    m1, m2 = (d // 2, d // 2 + 1)
    m = []
    for i, j in enumerate(arr):
        count += j
        if not m and m1 <= count:
            m.append(i)
        if m2 <= count:
            m.append(i)
            break
    return m[-1] * 2 if d % 2 else sum(m)


def activityNotifications(expenditure, d):
    srt = [0] * 201
    count = 0
    for i in expenditure[:d]:
        srt[i] += 1
    for i, v in enumerate(expenditure[d:]):
        limit = getLimit(srt, d)
        if v >= limit:
            count += 1
        srt[v] += 1
        srt[expenditure[i]] -= 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    e = list(map(int, input().rstrip().split()))

    result = activityNotifications(e, d)

    fptr.write(str(result) + '\n')

    fptr.close()
