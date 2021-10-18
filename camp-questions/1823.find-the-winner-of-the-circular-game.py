#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [False]+[True]*n
        def find_next(i=0)->int:
            count = 0
            while count < k:
                i += 1
                i %= (n+1)
                if players[i]:
                    count += 1
            return i
        def kill_one(i, left):
            nonlocal players, n
            if left == 1:
                return players.index(True)
            ind = find_next(i)
            players[ind] = False
            return kill_one(ind, left-1)
        return kill_one(0, n)
            
print(Solution().findTheWinner(6, 5))
# @lc code=end

