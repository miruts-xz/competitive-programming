from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        width = len(grid[0])
        n = 0
        count = 0
        while m >= 0 and n < width:
            if grid[m][n] < 0:
                count += (width - n)
                m -= 1
                continue
            n += 1
        return count
