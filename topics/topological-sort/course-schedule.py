class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj_list = [[] for _ in range(numCourses)]
        count = [0]*numCourses
        for c, pr in prerequisites:
            adj_list[pr].append(c)
            count[c] += 1
        q = deque()
        for i in range(numCourses):
            if count[i] == 0:
                q.append(i)
        taken = 0
        while q:
            c = q.popleft()
            taken += 1
            for a in adj_list[c]:
                count[a] -= 1
                if count[a] == 0:
                    q.append(a)
        return taken == numCourses
