from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        l = []
        h = 0
        while h < len(heights):
            if h == len(heights) - 1:
                return h
            diff = heights[h + 1] - heights[h]
            if diff > 0:
                if bricks - diff >= 0:
                    heapq.heappush(l, -diff)
                    bricks -= diff
                    h += 1
                    continue
                if ladders > 0:
                    if not l:
                        ladders -= 1
                        h += 1
                        continue
                    mx = heapq.heappop(l)
                    if diff >= -mx:
                        heapq.heappush(l, mx)
                        ladders -= 1
                        h += 1
                        continue
                    bricks += -mx
                    ladders -= 1
                    continue
                return h
            h += 1


s = Solution()
print(s.furthestBuilding([1, 13, 1, 1, 13, 5, 11, 11], 10, 8))
