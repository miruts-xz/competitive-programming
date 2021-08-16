# Created by miruts on 8/16/2021. Copyright 2021, All rights reserved.
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            srt = ''.join(sorted(s))
            res[srt].append(s)
        return list(res.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(['eat', 'ate', 'cat', 'act']))
