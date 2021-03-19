
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        rc = [0]*(len(s)+1)
        for i in range(1, len(s)+1):
            rc[i] = rc[i-1]+ abs(ord(t[i-1]) - ord(s[i-1]))
        mx = 0
        i, j = 0, 0
        while j < len(rc):
            if rc[j]-rc[i] <= maxCost:
                mx = max(mx, j-i)
                j += 1
            else:
                i += 1
        return mx
