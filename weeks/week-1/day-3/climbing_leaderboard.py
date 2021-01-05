#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


# Method solves climbing leaderboard problem from
# @https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbing_leaderboard(ranked: List[int], player: List[int]) -> List[int]:
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    ranks = []
    j = len(ranked) - 1
    rank = len(ranked) + 1
    for score in player:
        if len(ranks) > 0:
            rank = ranks[len(ranks) - 1]
        while score >= ranked[j] and rank > 1:
            rank -= 1
            j -= 1
        ranks.append(rank)
    return ranks


print(climbing_leaderboard([100, 100, 40, 40, 20, 10], [5, 25, 50, 120]))
