from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        [1, 2, 2]
        n = len(nums)
        res = []
        for i in range(2 ** n):
            b = bin(i)[2:]
            b = b.zfill(n)
            ss = [nums[j] for j in range(n) if b[j] == '1']
            if ss in res:
                continue
            res.append(ss)
        return res


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 3, 4, 5, 6]))
