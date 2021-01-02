#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = 0
    if len(s) <= 1:
        if s == 'a':
            return n
        else:
            return 0
    repeated = n // len(s)
    added = n % len(s)
    a_count += repeated * (s.count('a'))
    a_count += s[:added].count('a')
    return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
