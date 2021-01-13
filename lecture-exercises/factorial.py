#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

def f(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 1
    return n * f(n - 1)


def factorial(n) -> int:
    prev = 1
    while n > 0:
        prev *= n
        n -= 1
    return prev


print(f(5))

print(factorial(5))
