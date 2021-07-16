# Created by mire on 7/16/21. Copyright 2021, All rights reserved.


from functools import cmp_to_key


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ordr = [0] * 26
        for i, l in enumerate(order):
            ordr[ord(l) - ord('a')] = i

        def cmp(a, b) -> int:
            if ordr[ord(a) - ord('a')] < ordr[ord(b) - ord('a')]:
                return -1
            if ordr[ord(a) - ord('a')] > ordr[ord(b) - ord('a')]:
                return 1
            return 0

        res = sorted(str, key=cmp_to_key(cmp))
        return ''.join(res)


if __name__ == "__main__":
    print(Solution().customSortString("denvar", "navermind"))
