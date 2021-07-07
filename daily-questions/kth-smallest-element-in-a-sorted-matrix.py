from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        larr = []
        for l in matrix:
            larr += l
        larr.sort()
        return larr[k - 1]


if __name__ == "__main__":
    print(Solution().kthSmallest([[1, 2, 3], [2, 4, 5], [3, 5, 6]], 3))
