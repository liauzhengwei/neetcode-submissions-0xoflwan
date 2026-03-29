import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # compute the square root of every point
        # create a heap storing (coords, dist)
        # return the k closest points AKA first k values in the min heap
        lst = []
        
        for point in points:
            dist = math.sqrt( ((point[0] - 0) ** 2) + ((point[1] - 0) ** 2))
            tup = (dist, point)

            lst.append(tup)

        heapq.heapify(lst)
        
        result = []
        for i in range(k):
            newTup = heapq.heappop(lst)
            result.append(newTup[1])

        return result