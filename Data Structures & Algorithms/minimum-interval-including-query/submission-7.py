class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q,i) for i,q in enumerate(queries))

        res = [-1] * len(queries)

        heap = []
        n = len(intervals)
        i = 0

        for q, idx in sorted_queries:
            while i < n and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(heap, (r-l+1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res
