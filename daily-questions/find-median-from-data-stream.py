# Created by mire on 7/11/21. Copyright 2021, All rights reserved.
from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.above_md = []
        self.below_md = []
        self.prev_median = None

    def addNum(self, num: int) -> None:
        if not self.prev_median:
            self.prev_median = num
        if not self.below_md:
            heappush(self.below_md, -num)
        else:
            if num <= self.prev_median:
                heappush(self.below_md, -num)
            else:
                heappush(self.above_md, num)

            while abs(len(self.below_md) - len(self.above_md)) > 1:
                if len(self.below_md) > len(self.above_md):
                    heappush(self.above_md, -heappop(self.below_md))
                else:
                    heappush(self.below_md, -heappop(self.above_md))
            if len(self.below_md) == len(self.above_md):
                self.prev_median = (-self.below_md[0] + self.above_md[0]) / 2
            elif len(self.below_md) > len(self.above_md):
                self.prev_median = -self.below_md[0]
            else:
                self.prev_median = self.above_md[0]

    def findMedian(self) -> float:
        return self.prev_median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
