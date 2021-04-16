class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        ln = len(obstacles)-1
        q = deque()
        visited = set()
        visited.add((2, 0))
        q.append((2, 0, 0))
        while q:
            lane, point, cost = q.popleft()
            if point == ln:
                return cost
            if obstacles[point+1] != lane:
                visited.add((lane, point+1))
                q.append((lane, point+1, cost))
            for n in self.getNeighbors(lane):
                if obstacles[point] != n and (n, point) not in visited:
                    visited.add((n,point))
                    q.append((n, point, cost+1))
        
    def getNeighbors(self, cur)-> List[int]:
        if cur == 1:
            return [2, 3]
        if cur == 2:
            return [1, 3]
        return [2, 1]
