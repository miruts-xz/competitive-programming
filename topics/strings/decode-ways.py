class Solution:
    def numDecodings(self, s: str) -> int:
        return self.decodeWays(0, s)
    def decodeWays(self, index, s) -> int:
        if index == len(s):  
            return 1
        if s[index] == '0':  
            return 0
        if index == len(s)-1: 
            return 1
        answer = self.decodeWays(index + 1, s)                                
        if int(s[index : index + 2]) <= 26:			     
            answer += self.decodeWays(index + 2, s)
        return answer
