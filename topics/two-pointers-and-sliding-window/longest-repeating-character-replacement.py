class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = set()
        mx = 0
        for i in range(len(s)):
            cur_k = k
            letter = s[i]
            if letter in st:
                continue
            st.add(letter)
            l = i
            r = i+1
    
            while r < len(s):
                if s[r] == letter:
                    r += 1
                    mx = max(mx, r-l)
                elif cur_k > 0:
                    r += 1
                    mx = max(mx,r-l)
                    cur_k -= 1
                else:
                    if s[l] != letter:
                        cur_k += 1
                    l += 1
            l = i-1
            while l >= 0:
                if s[l] == letter:
                    l -= 1
                    mx = max(r-l-1,mx)
                elif cur_k > 0:
                    cur_k -= 1
                    l -= 1
                    mx = max(r-l-1, mx)
                else:
                    break
        return mx
