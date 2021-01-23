import heapq


#
# Complete the runningMedian function below.
#
def runningMedian(a):
    r = []
    minHeap = []
    maxHeap = []
    if len(a) < 2:
        return a
    r.append(a[0] / 1.0)
    elem1, elem2 = a[0], a[1]
    if elem1 > elem2:
        heapq.heappush(minHeap, elem1)
        heapq.heappush(maxHeap, -1 * elem2)
    else:
        heapq.heappush(maxHeap, -1 * elem1)
        heapq.heappush(minHeap, elem2)
    md = (elem1 + elem2) / 2
    r.append(round(md, 1))
    for n in a[2:]:
        if n > md:
            heapq.heappush(minHeap, n)
        else:
            heapq.heappush(maxHeap, -1 * n)
        while abs(len(maxHeap) - len(minHeap)) > 1:
            if len(maxHeap) > len(minHeap):
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
            else:
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))
        if len(maxHeap) == len(minHeap):
            md = (-1 * maxHeap[0] + minHeap[0]) / 2.0
        elif len(maxHeap) > len(minHeap):
            md = -1 * maxHeap[0]
        else:
            md = minHeap[0] / 1.0
        r.append(round(md, 1))
    return r
