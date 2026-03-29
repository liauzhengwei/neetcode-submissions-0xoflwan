import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            heapq.heappop(self.minheap)


    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heapreplace(self.minheap, val)
        return self.minheap[0]

"""
    def __init__(self, k: int, nums: List[int]):
        self.numArr = sorted(nums)
        self.kth = k

    def add(self, val: int) -> int:
        self.numArr.append(val)
        self.numArr.sort()
        return self.numArr[len(self.numArr) - self.kth]

        #[1,2,3,4,5]
        #kth = 2
        #5 - 2 = 3
"""
