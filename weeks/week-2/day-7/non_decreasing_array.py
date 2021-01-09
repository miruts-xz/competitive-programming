#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Method implements non decreasing array leetcode challenge @https://leetcode.com/problems/non-decreasing-array
def non_decreasing(nums: List[int]) -> bool:
    count = 0
    for i in range(len(nums) - 1):
        if not nums[i] <= nums[i + 1]:
            if count < 1:
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                    count += 1
                elif i > 0 and nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                    count += 1
                elif i == 0:
                    nums[i] = nums[i + 1]
                    count += 1
            else:
                return False
    return True


print(non_decreasing([5, 7, 1, 8]))
