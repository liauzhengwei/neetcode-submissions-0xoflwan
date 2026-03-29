import heapq

class MedianFinder:

    def __init__(self):
      self.maxheap = []
      self.minheap = []  

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0 or (num > self.minheap[0]):
            self.minheap.append(num)
            heapq.heapify(self.minheap)
        else:
            self.maxheap.append(-num)
            heapq.heapify(self.maxheap)
        
        if abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                val = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -val)
                heapq.heapify(self.maxheap)

            elif len(self.maxheap) > len(self.minheap):
                val = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, val)
                heapq.heapify(self.minheap)

    def findMedian(self) -> float:
        # Get max of minheap and min of maxheap
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]