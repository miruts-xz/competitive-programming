from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        running_sum = [0] * (len(weights) + 1)
        for i, v in enumerate(weights):
            running_sum[i + 1] = weights[i] + running_sum[i]
        mn = max(weights)
        mx = running_sum[-1]
        l = mn
        r = mx
        min_weight = mx
        while l <= r:
            mid = l + (r - l) // 2
            d = self.getDays(running_sum, mid)
            print(mid, d)
            if d <= D:
                min_weight = min(min_weight, mid)
                r = mid - 1
            else:
                l = mid + 1
        return min_weight

    def getDays(self, running: List[int], weight) -> int:
        i = 0
        temp = weight
        curr = 0
        while curr != len(running) - 1:
            l = curr
            r = len(running) - 1
            curr = l
            while l <= r:
                mid = l + (r - l) // 2
                if running[mid] <= weight:
                    curr = max(curr, mid)
                    l = mid + 1
                else:
                    r = mid - 1

            i += 1
            weight = running[curr] + temp
        return i
