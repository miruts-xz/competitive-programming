#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Method implements factorial Hackerrank challenge @https://www.hackerrank.com/challenges/30-recursion/problem
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
