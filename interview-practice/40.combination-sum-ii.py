#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(comb, remain, curr, results):
            if remain == 0:
                results.append(list(comb))
            if remain <= 0: return
            
            for next_curr in range(curr, len(candidates)):
                
                if next_curr > curr and candidates[next_curr]==candidates[next_curr-1]: continue
                pick = candidates[next_curr]
                if remain - pick < 0: break
                comb.append(pick)
                backtrack(comb, remain-pick, next_curr+1, results)
                comb.pop()
        candidates.sort()
        results = list()
        backtrack([], target, 0, results)
        return results

# @lc code=end
# solved in 35 minues, but was a bit inefficient at first

