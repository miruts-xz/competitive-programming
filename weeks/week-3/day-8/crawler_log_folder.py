class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for l in logs:
            if l == '../':
                if c:
                    c -= 1
            elif l != './':
                c += 1
        return c
