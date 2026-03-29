class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap using negatives as Python only has min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Change back to positive when popping from max heap
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                # Change back to negative when pushing into max heap
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0