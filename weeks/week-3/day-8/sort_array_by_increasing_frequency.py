from functools import cmp_to_key
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1
        tuple_list = []
        for i, v in freq_dict.items():
            tuple_list.append((i, v))
        srt = sorted(tuple_list, key=cmp_to_key(self.compare))
        result = []
        for t in srt:
            for j in range(t[1]):
                result.append(t[0])
        return result

    def compare(self, x, y):
        if x[1] > y[1]:
            return 1
        elif x[1] == y[1]:
            return y[0] - x[0]
        return -1
