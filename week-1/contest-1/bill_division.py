#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total_price = 0
    for i in bill:
        total_price += i
    anas_eaten_prices = total_price - bill[k]
    share = anas_eaten_prices//2
    if b == share:
        print("Bon Appetit")
    else:
        change = b-share
        print(change)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
