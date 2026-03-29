"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Need to check if there are any conflicts
        ## Conflicts occur when overlaps
        ## Overlaps occur when the start of the current is less than the end of the previous
        if not intervals:
            return True

        can_add = True

        sorted_int = sorted(intervals, key=lambda x:x.end)
        prev_end = sorted_int[0].end

        for i in range(1, len(intervals)):
            start = sorted_int[i].start
            end = sorted_int[i].end
            if start < prev_end:
                can_add = False
            else:
                prev_end = end

        return can_add