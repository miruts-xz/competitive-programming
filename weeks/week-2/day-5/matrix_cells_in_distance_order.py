#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def all_cells_dist_order(R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    dict = {}
    for r in range(R):
        for c in range(C):
            dict[(r, c)] = abs(r - r0) + abs(c - c0)
    arr: List[tuple] = sorted(dict.items(), key=lambda x: x[1])
    return [[k[0], k[1]] for k, _ in arr]


print(all_cells_dist_order(1, 2, 0, 0))
