# Created by miruts at 8/10/2021

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        memo = {}
        def getCount(i, oned=False) -> int:
            nonlocal memo, s
            res = 0
            if i >= len(s):
                return 0
            if memo.get((i, oned), None) is not None:
                return memo.get((i, oned))
            if not oned and s[i] == '1':
                res = min(getCount(i + 1, oned) + 1, getCount(i + 1, True))
            elif not oned and s[i] == '0':
                res = min(getCount(i + 1, True) + 1, getCount(i + 1, oned))
            elif oned and s[i] == '1':
                res = getCount(i + 1, oned)
            else:
                res = getCount(i + 1, oned) + 1
            memo[(i, oned)] = res
            return res
        return getCount(0)


if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr('10010010'))
