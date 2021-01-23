import heapq


#
# Complete the cookies function below.
#
def cookies(k, A):
    minHeap = A
    heapq.heapify(A)
    count = 0
    while minHeap[0] < k and len(minHeap) > 1:
        l1 = heapq.heappop(minHeap)
        l2 = heapq.heappop(minHeap)
        heapq.heappush(minHeap, l1 + 2 * l2)
        count += 1
    return count if minHeap[0] >= k else -1
