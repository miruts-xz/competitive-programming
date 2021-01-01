# Defines a program to print left justified stars
from typing import List


def triangle1(n: int):
    for i in range(1, n + 1):
        print('{}'.format('*' * i), end='\n')


triangle1(10)

