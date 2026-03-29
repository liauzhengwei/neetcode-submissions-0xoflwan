"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x:x.start)

        # Min heap to track ending times
        heap = []

        for interval in intervals:
            # If the earliest ending meeting ends before current starts
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap) # Reuse the room
            
            heapq.heappush(heap, interval.end)

        return len(heap)