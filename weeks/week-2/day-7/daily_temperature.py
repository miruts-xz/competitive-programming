#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Method implements daily temperature leetcode challenge @https://leetcode.com/problems/daily-temperatures
def daily_temperature(T: List[int]) -> List[int]:
    stack = []
    result = [0] * len(T)
    for i in range(len(T)):
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) > 0 and T[stack[len(stack) - 1]] < T[i]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
    while len(stack) > 0:
        result[stack.pop()] = 0
    return result


print(daily_temperature([73, 74, 75, 69, 71, 72, 76, 73]))
