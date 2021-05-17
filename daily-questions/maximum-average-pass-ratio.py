import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        total = 0.0
        hp = []
        for p, t in classes:
            heapq.heappush(hp, (-(t-p)/(t*t+t), p, t))
        ex = extraStudents
        while ex > 0:
            _, p,t = heapq.heappop(hp)
            p = p+ 1
            t = t+ 1
            heapq.heappush(hp, (-(t-p)/(t*t+t), p, t))
            ex -= 1
        while hp:
            _, p, t = heapq.heappop(hp)
            total += p/t
        return total/len(classes)
