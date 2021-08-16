# Created by miruts on 8/16/2021. Copyright 2021, All rights reserved.
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_len = len(t)
        s_len = len(s)
        if t_len > s_len:
            return ""
        ans = ""
        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        w_freq = defaultdict(int)
        for i in range(t_len):
            w_freq[s[i]] += 1
        l = 0
        r = t_len - 1
        # print(t_freq, w_freq)
        while l <= s_len - t_len + 1 and r < s_len:
            satisfy = True
            for k, v in t_freq.items():
                if w_freq[k] < v:
                    satisfy = False
                    break
            if satisfy:
                new = s[l:r + 1]
                ans = new if ans == "" or len(new) < len(ans) else ans
                w_freq[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < s_len:
                    w_freq[s[r]] += 1
        return ans


if __name__ == "__main__":
    print(Solution().minWindow("whatever", "eve"))
