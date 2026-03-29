import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        
        while len(max_heap) > 1:
            heapq.heapify(max_heap)

            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first > second:
                left = first - second
                max_heap.append(-left)
            # elif first == second
                # nothing happens
        
        return -max_heap[0] if max_heap else 0