class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                count += 1
            else:
                prev_end = max(end, prev_end)

        return count
