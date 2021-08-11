# Created by miruts on 8/11/2021. Copyright 2021, All rights reserved.
from collections import defaultdict
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1
        arr.sort(key=lambda x: abs(x))
        for i in range(len(arr)):
            if not freq.get(arr[i]):
                continue
            p1 = arr[i]
            if freq.get(2 * p1):
                freq[p1] -= 1
                freq[p1 * 2] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().canReorderDoubled([2, 4, 2, 6, 7, 14]))
