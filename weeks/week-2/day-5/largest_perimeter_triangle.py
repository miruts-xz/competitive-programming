#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def largest_perimeter(A: List[int]) -> int:
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2] and A[i] + A[i + 2] > A[i + 1] and A[i + 1] + A[i + 2] > A[i]:
            return A[i] + A[i + 2] + A[i + 1]
    return 0


print(largest_perimeter([2, 3, 4, 5, 6, 7]))
