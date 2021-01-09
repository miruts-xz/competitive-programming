#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


# Method implements h index leetcode challenge @https://leetcode.com/problems/h-index
def h_index(citations: List[int]) -> int:
    i, n = 0, len(citations)
    citations.sort()
    while i < n:
        if citations[i] >= n - i:
            return n - i
    return 0
