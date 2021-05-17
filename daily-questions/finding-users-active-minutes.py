class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0]*(k)
        counts = {}
        for u, m in logs:
            s = counts.get(u, set())
            s.add(m)
            counts[u] = s
        for s in counts.values():
            answer[len(s)-1] += 1
        return answer
