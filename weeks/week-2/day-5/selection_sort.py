#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List

# Implements selection sort algorithm
def selection_sort(a: List[int]) -> List[int]:
    for i in range(len(a)):
        n = i
        for j in range(i + 1, len(a)):
            if a[j] < a[n]:
                n = j
        a[i], a[n] = a[n], a[i]
    return a
