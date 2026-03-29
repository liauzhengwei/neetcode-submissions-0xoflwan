class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x:x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # If current interval overlaps with previous
            if start < prev_end:
                count+=1    # Remove current interval
            else:
                prev_end = end # Keep current interval and update end
        
        return count