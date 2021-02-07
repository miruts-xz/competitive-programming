def longest_substring(s: str) -> int:
    longest = 0
    for i in range(len(s)):
        if longest > len(s) - i:
            return longest
        subs = [s[i]]
        for j in s[i + 1:]:
            if j not in subs:
                subs.append(j)
            else:
                break
        if len(subs) > longest:
            longest = len(subs)
    return longest


print(longest_substring('ababaababa'))
# def longest_substr(s: str) -> int:
#     low_index, high_index = 0, 0
#     subs = []
#     for i in range(len(s)):
#         subs.append(low)
