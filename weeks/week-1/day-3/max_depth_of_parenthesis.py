#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)

# Method implements maximum depth of parenthesis leetcode challenge
# @https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses:
def max_depth(s: str) -> int:
    m = 0
    temp_max = 0
    for c in s:
        if c == '(':
            temp_max += 1
            m = max(m, temp_max)
        elif c == ")":
            temp_max -= 1
    return m


print(max_depth("(1+(2*3)+((8)/4))+1"))
