from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        sd = {}
        for i in range(len(position)):
            sd[position[i]] = speed[i]
        position.sort()
        time = []
        for p in position:
            time.append((target - p) / sd.get(p))
        count = 1
        mx = time[len(time) - 1]
        for i in range(len(time) - 1, 0, -1):
            if time[i - 1] <= mx:
                continue
            mx = max(mx, time[i - 1])
            count += 1
        return count
