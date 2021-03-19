class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)
        l = r = 0
        seen = set()
        while l < n and r < n:
          if s[r] not in seen:
            seen.add(s[r])
            r += 1
            longest = max(longest, r-l)
          else:
            seen.remove(s[l])
            l += 1
        return longest
    
