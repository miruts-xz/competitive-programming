#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List
import math


# Method implements k closest points to origin leetcode challenge
# @https://leetcode.com/problems/k-closest-points-to-origin
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    dist_dict = {}

    def dist(p2: List[int]) -> float:
        return math.sqrt(p2[0] ** 2 + p2[1] ** 2)

    for i in range(len(points)):
        dist_dict[i] = dist(points[i])
    sorted_list = sorted(dist_dict.items(), key=lambda x: x[1])
    r = []
    for v in sorted_list[:k]:
        r.append(points[v[0]])
    return r


print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
