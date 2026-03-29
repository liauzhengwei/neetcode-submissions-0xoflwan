class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)

            if i >= k - 1:
                result.append(-heap[0][0])

        return result 