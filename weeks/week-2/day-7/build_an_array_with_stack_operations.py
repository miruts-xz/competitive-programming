#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        real_result = []
        i = 1
        while i <= n and real_result != target:
            if i in target:
                result.append('Push')
                real_result.append(i)
            else:
                result.append('Push')
                result.append('Pop')
            i += 1
        return result


print(Solution().buildArray([3, 5, 6], 9))
