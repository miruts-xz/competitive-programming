class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        strlen = len(strs[0])
        count = 0
        for i in range(strlen):
            for j in range(n-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
        return count
