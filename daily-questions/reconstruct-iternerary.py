# Created by mire on 7/16/21. Copyright 2021, All rights reserved.

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        paths, counts = {}, {}
        for t in tickets:
            paths[t[0]] = paths.get(t[0], []) + [t[1]]
            counts[tuple(t)] = counts.get(tuple(t), 0) + 1
            paths[t[1]] = paths.get(t[1], [])

        for val in paths.values():
            val.sort()

        path = ['JFK']

        def dfs(cur: str):
            nonlocal paths, counts, path
            if len(path) == len(tickets) + 1:
                return path

            for p in paths[cur]:
                edge = (cur, p)
                if counts[edge] > 0:
                    path.append(p)
                    counts[edge] -= 1
                    res = dfs(p)
                    if res:
                        return res
                    counts[edge] += 1
                    path.pop()
            return None

        return dfs("JFK")


if __name__ == "__main__":
    print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
