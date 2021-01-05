#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mached_socks = {}
    for i in range(len(ar)):
        curr = ar[i]
        if curr in mached_socks.keys():
            continue
        count = 1
        for j in range(i+1, len(ar)):
            if curr == ar[j]:
                count +=1
        if(count > 1):
            mached_socks[curr] = count//2
    mached_socks_count = 0
    for k, v in mached_socks.items():
        mached_socks_count += v
    return mached_socks_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
