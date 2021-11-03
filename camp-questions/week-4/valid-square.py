import math
from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def _validSquare(p1, p2, p3, p4)->bool:
            def get_dist(p1, p2):
                return math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)
            top2 = get_dist(p1, p2)
            top3 = get_dist(p1, p3)
            top4 = get_dist(p1, p4)
            if 0 in [top2, top3, top4]: return False
            valid = False
            if top2 == top3:
                return abs(top4 - math.sqrt(top2**2+top3**2)) < 10**-5
            if top2 == top4:
                return abs(top3 - math.sqrt(top2**2+top4**2)) < 10**-5
            if top3 == top4:
                return abs(top2 - math.sqrt(top3**2+top4**2)) < 10**-5
            return False
        return _validSquare(p1, p2, p3, p4) and _validSquare(p2, p1, p3,p4) and _validSquare(p3, p1, p4, p2)