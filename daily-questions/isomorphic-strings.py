# Created by mire on 7/12/21. Copyright 2021, All rights reserved.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        rv_mp = {}
        for i, c in enumerate(s):
            if not mp.get(c):
                if rv_mp.get(t[i]) and rv_mp[t[i]] != c:
                    return False
                mp[c] = t[i]
                rv_mp[t[i]] = c
            elif mp[c] != t[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("ababa", "babab"))
