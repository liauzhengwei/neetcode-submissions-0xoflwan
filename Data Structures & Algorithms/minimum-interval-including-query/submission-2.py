class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # For each query, find the smallest interval length that contains q
        # return -1 if none
        ## use Sorting + Min heap

        # Sort intervals by start, sort queries, use min heap
        ## Add all intervals that start before it and Remove intervals that end before it
        ## heap top = smallest valid interval

        intervals.sort()
        sorted_queries = sorted((q,i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        heap = [] # (length, end)

        i = 0
        n = len(intervals)

        for q, idx in sorted_queries:
            # Add valid intervals
            while i < n and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(heap, (r-l + 1, r))
                i += 1
            
            # Remove invalid intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Get answer
            if heap:
                res[idx] = heap[0][0]

        return res
