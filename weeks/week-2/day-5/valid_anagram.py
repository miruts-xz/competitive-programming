#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)


def isAnagram(s: str, t: str) -> bool:
    a = [0] * 27
    b = [0] * 27
    for c in s:
        a[ord(c) % 27] += 1
    for c in t:
        b[ord(c) % 27] += 1
    return a == b


print(isAnagram('anagram', 'naagram'))
