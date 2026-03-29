class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time
        intervals.sort()

        # Sort queries but keep original indices
        sorted_queries = sorted([(q,i) for i,q in enumerate(queries)])

        # Min heap: (interval_length, end_time)
        min_heap = []
        result = [-1] * len(queries)

        i=0 # Pointer for intervals

        for query, original_idx in sorted_queries:
            # Add all intervals that start <= current query to the heap
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(min_heap, (length, end))
                i += 1

            # Remove all intervals that end < current query (expired in intervals)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # The top of heap is the smallest valid interest
            if min_heap:
                result[original_idx] = min_heap[0][0]
            else:
                result[original_idx] = -1

        return result