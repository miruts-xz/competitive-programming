#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(h):
    mx = h[0]
    for i in range(len(h)):
        count = 1
        k = i - 1
        curr = h[i]
        while k >= 0:
            if not h[k] >= curr:
                break
            count += 1
            k -= 1
        j = i + 1
        while j < len(h):
            if not h[j] >= curr:
                break
            count += 1
            j += 1
        mx = max(mx, count * curr)
    return mx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
