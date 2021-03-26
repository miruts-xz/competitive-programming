class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        count = [0]*numCourses
        for c, pr in prerequisites:
            adj_list[pr].append(c)
            count[c] += 1
        # print(adj_list)
        q = deque()
        for i in range(numCourses):
            if count[i] == 0:
                q.append(i)
        taken = 0
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            taken += 1
            for a in adj_list[c]:
                count[a] -= 1
                if count[a] == 0:
                    q.append(a)
        return res if taken == numCourses else []
