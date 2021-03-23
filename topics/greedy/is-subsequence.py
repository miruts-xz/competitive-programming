class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        last = s[len(s)-1]
        siter = 0
        for i in range(len(t)):
            if t[i] == s[siter]:
                siter += 1
            if siter > len(s)-1:
                break
        
        return True if siter == len(s) else False
        
