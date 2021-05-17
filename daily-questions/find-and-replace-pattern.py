class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for w in words:
            ws = {}
            bck = {}
            valid = True
            for i in range(len(w)):
                cw = w[i]
                cp = pattern[i]
                mp = ws.get(cp)
                rev = bck.get(cw)
                if mp != None and mp != cw or rev != None and rev != cp:
                    valid = False
                    break
                ws[cp] = cw
                bck[cw] = cp
            if valid:
                answer.append(w)
        return answer
