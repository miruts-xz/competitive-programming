from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = {}
        for w in words:
            freq_dict[w] = freq_dict.get(w, 0) + 1
        r = []
        freq_dict = sorted(freq_dict.items())
        srt = sorted(freq_dict, key=lambda x: x[1], reverse=True)
        for i in range(k):
            r.append(srt[i][0])
        return r
