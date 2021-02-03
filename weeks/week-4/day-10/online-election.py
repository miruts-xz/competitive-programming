from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        prev_max = 0
        person_votes = [0] * 5000
        self.time_to_max = {}
        for i in range(len(times)):
            prev = person_votes[persons[i]]
            curr = prev + 1
            person_votes[persons[i]] = curr
            if curr >= prev_max:
                self.time_to_max[times[i]] = persons[i]
                prev_max = curr
            else:
                self.time_to_max[times[i]] = self.time_to_max[times[i - 1]]

    def q(self, t: int) -> int:
        idx = self.getIndex(t)
        return self.time_to_max[self.times[idx]]

    def getIndex(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        result = l
        while l <= r:
            mid = l + (r - l) // 2
            if self.times[mid] <= t:
                result = max(result, mid)
                l = mid + 1
            else:
                r = mid - 1
        return result
