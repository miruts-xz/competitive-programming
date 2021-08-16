from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.running_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.running_sum[i + 1] = self.running_sum[i] + nums[i]
        # print(self.running_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum[right + 1] - self.running_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


if __name__ == '__main__':
    obj = NumArray([1, 2, 3, 4, 5, 4, 2])
    print(obj.sumRange(0, 2))
