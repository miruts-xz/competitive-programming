#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) <= 1:
            return S
        i = 1
        while i < len(S):
            if S[i] == S[i - 1]:
                S = S[:i - 1] + S[i + 1:]
                if i > 1:
                    i -= 1
                continue
            i += 1
        return S
