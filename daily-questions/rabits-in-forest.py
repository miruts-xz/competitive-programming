class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = {}
        count = 0
        for a in answers:
            if seen.get(a):
                seen[a] -= 1
            else:
                count += a+1
                seen[a] = a
        return count
