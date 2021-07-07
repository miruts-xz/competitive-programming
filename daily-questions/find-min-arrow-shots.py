from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = len(points)
        end = points[0][1]
        for p in points[1:]:
            if p[0] <= end:
                count -= 1
            else:
                end = p[1]
        return count


if __name__ == "__main__":
    print(Solution().findMinArrowShots([[2, 6], [2, 8], [7, 12], [10, 11], [10, 13]]))
