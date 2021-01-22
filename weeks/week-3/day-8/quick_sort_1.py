#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left = []
    equal = []
    right = []
    for a in arr:
        if a < p:
            left.append(a)
        elif a > p:
            right.append(a)
        else:
            equal.append(a)
    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
