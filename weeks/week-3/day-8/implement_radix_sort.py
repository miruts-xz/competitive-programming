from typing import List
from functools import cmp_to_key


def radix_sort(nums: List[int]) -> List[int]:
    mx = len(str(max(nums)))
    for i in range(1, mx + 1):
        nums = sorted(nums, key=cmp_to_key(predicate_to_compare(i)))
        print('step {}'.format(i), nums)
    return nums


# Method generates compare functions based on radix
def predicate_to_compare(r):
    def compare(x, y):
        if x % (10 ** r) > y % (10 ** r):
            return 1
        elif x % (10 ** r) < y % (10 ** r):
            return -1
        return 0

    return compare


print(radix_sort([4, 3, 5, 66, 777, 88, 90, 100]))
