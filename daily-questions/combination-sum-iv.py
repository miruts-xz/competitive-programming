class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.recurse(nums,0,memo, target)
    def recurse(self,nums,idx,memo, target):
        if target == 0:
            return 1
        elif target < 0:
            return 0
        if memo.get((idx,target), None) is not None:
            return memo.get((idx,target))
        total = 0
        for i in range(len(nums)):
            total += self.recurse(nums,i,memo, target-nums[i])
        memo[(idx,target)] = total
        return total
