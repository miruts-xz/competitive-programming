from typing import List
from math import inf
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1, p2):
            if p2[0]-p1[0] == 0:
                return inf
            return (p2[1]-p1[1])/(p2[0]-p1[0])
        last = coordinates[-1]
        prev = slope(coordinates[0], last)
        for i in range(1, len(coordinates)-1):
            if slope(coordinates[i], last) != prev:
                return False
        return True