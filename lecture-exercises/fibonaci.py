#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

def fibo(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)


def fibo_i(n: int) -> int:
    prev0, prev1, count = 0, 1, 0
    while count < n - 1:
        temp = prev1
        prev1 = prev0 + prev1
        prev0 = temp
        count += 1
    return prev1


print(fibo(6))
print(fibo_i(6))
