import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.md = None

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            self.minHeap.append(num)
            self.md = num
        elif num < self.md:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        while abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) == len(self.minHeap):
            self.md = (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            self.md = self.minHeap[0]
        else:
            self.md = -self.maxHeap[0]
        return self.md
