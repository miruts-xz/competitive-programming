from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        freq_map = {}
        for a in arr:
            freq_map[a] = freq_map.get(a, 0) + 1
        srt = sorted(freq_map.items(), key=lambda x: -x[1])
        srtlen = len(srt)
        # print(srt)
        s = 0
        for i in range(len(srt)):
            s += srt[i][1]
            if s >= n // 2:
                return i + 1


if __name__ == "__main__":
    print(Solution().minSetSize([1, 2, 2, 4, 5, 5, 5]));
