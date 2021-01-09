#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Method implements distant barcodes leetcode challenge @https://leetcode.com/problems/distant-barcodes
def distant_barcodes(barcodes: List[int]) -> List[int]:
    if len(barcodes) == 1:
        return barcodes
    i = 1
    while i < len(barcodes):
        if barcodes[i] == barcodes[i - 1]:
            if barcodes[i] != barcodes[len(barcodes) - 1]:
                barcodes = barcodes[:i] + barcodes[i + 1:] + barcodes[i:i + 1]
                continue
            elif barcodes[i] != barcodes[0]:
                barcodes = barcodes[i:i + 1] + barcodes[:i] + barcodes[i + 1:]
                continue
            j = i + 1
            re = False
            while j < len(barcodes) - 1:
                if barcodes[j] != barcodes[i] and barcodes[j + 1] != barcodes[i]:
                    barcodes = barcodes[:i] + barcodes[i + 1:j + 1] + barcodes[i:i + 1] + barcodes[j + 1:]
                    re = True
                    break
                j += 1
            j = i - 2
            if not re:
                while j > 0:
                    if barcodes[i] != barcodes[j] and barcodes[j - 1] != barcodes[i]:
                        barcodes = barcodes[:j] + barcodes[i:i + 1] + barcodes[j:i] + barcodes[i + 1:]
                        re = True
                        break
                    j -= 1
            if re:
                continue
        i += 1
    return barcodes


print(distant_barcodes(
    [51, 83, 51, 40, 51, 40, 51, 40, 83, 40, 83, 83, 51, 40, 40, 51, 51, 51, 40, 40, 40, 83, 51, 51, 40, 51, 51, 40, 40,
     51, 51, 40, 51, 51, 51, 40, 83, 40, 40, 83, 51, 51, 51, 40, 40, 40, 51, 51, 83, 83, 40, 51, 51, 40, 40, 40, 51, 40,
     83, 40, 83, 40, 83, 40, 51, 51, 40, 51, 51, 51, 51, 40, 51, 83, 51, 83, 51, 51, 40, 51, 40, 51, 40, 51, 40, 40, 51,
     51, 51, 40, 51, 83, 51, 51, 51, 40, 51, 51, 40, 40]))
