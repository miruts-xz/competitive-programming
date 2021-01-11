#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ['{', '[', '(']:
            stack.append(c)
        else:
            try:
                char = stack.pop()
                if char == '(':
                    if c != ')':
                        return False
                elif char == '{':
                    if c != '}':
                        return False
                else:
                    if c != ']':
                        return False
            except:
                return False
    if len(stack) > 0:
        return False
    return True


print(isValid('()'))
