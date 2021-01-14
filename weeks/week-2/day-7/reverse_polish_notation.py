import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for t in tokens:
            if t.isdigit() or t.startswith('-') and len(t) > 1:
                result.append(int(t))
                continue
            op1 = result.pop()
            op2 = result.pop()
            if t == '*':
                result.append(op2 * op1)
            elif t == '-':
                result.append(op2 - op1)
            elif t == '/':
                r = (op2 / op1)
                if r < 0:
                    r = math.ceil(r)
                else:
                    r = math.floor(r)
                result.append(r)
            elif t == '+':
                result.append(op2 + op1)
        return result.pop()
