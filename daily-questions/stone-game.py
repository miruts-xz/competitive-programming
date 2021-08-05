from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        memo = {}
        th = total // 2
        if self.stoneSum(piles, memo, 0, len(piles) - 1) > th:
            return True
        return False

    def stoneSum(self, piles: List[int], memo, l, r) -> int:
        if l >= r:
            return piles[l]
        if memo.get((l, r), None):
            return memo.get((l, r))
        m = max(piles[l] + self.stoneSum(piles, memo, l + 1, r), piles[r] + self.stoneSum(piles, memo, l, r - 1))
        memo[(l, r)] = m
        return m


if __name__ == "__main__":
    print(Solution().stoneGame([5, 3, 2, 1, 1, 3, 3]))
