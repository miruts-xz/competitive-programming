class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 1:
            return 0
        intervals.sort()
        # print(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        count = 0
        for st,ed in intervals[1:]:
            if self.overlap(start, end, st,ed):
                if ed < end:
                    end = ed
                    start = st
                count += 1
            else:
                end = ed
        return count
    def overlap(self,st1, ed1, st2, ed2):
        if st2 < ed1 or ed2 < ed1:
            return True
        return False
