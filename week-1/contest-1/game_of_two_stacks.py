#!/bin/python3
from typing import List
import os
import sys


#
# Complete the twoStacks function below.
#
def twoStacks(limit: int, a: List[int], b: List[int]) -> int:
    a_index, b_index, total_sum, count = 0, 0, 0, 0
    while a_index < len(a) and total_sum + a[a_index] <= limit:
        total_sum += a[a_index]
        a_index += 1
        count += 1
    while b_index < len(b) and a_index >= 0:
        total_sum += b[b_index]
        b_index += 1
        while a_index > 0 and total_sum > limit:
            a_index -= 1
            total_sum -= a[a_index]
        if total_sum <= limit and a_index + b_index > count:
            count = a_index + b_index
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
