#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Method implements reorganize string leetcode challenge @https://leetcode.com/problems/reorganize-string
def reorganize_string(s: str) -> str:
    if len(s) == 1:
        return s
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            if s[i] != s[len(s) - 1]:
                s = s[:i] + s[i + 1:] + s[i]
                continue
            elif s[i] != s[0]:
                s = s[i] + s[:i] + s[i + 1:]
                continue
            j = i + 1
            re = False
            while j < len(s) - 1:
                if s[j] != s[i] and s[j + 1] != s[i]:
                    s = s[:i] + s[i + 1:j + 1] + s[i] + s[j + 1:]
                    re = True
                    break
                j += 1
            j = i - 2
            if not re:
                while j > 0:
                    if s[i] != s[j] and [j - 1] != s[i]:
                        s = s[:j] + s[i] + s[j:i] + s[i + 1:]
                        re = True
                        break
                    j -= 1
            if not re:
                return ""
            else:
                continue
        i += 1
    return s


print(reorganize_string("abbabbaaab"))
