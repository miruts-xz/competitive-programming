from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1
        r = []
        srt = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            r.append(srt[i][0])
        return r
