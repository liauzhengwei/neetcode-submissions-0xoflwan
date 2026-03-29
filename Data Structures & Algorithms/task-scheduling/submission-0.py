import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        proc = {}
        for task in tasks:
            if task not in proc:
                proc[task] = 1
            else:
                proc[task] += 1
        
        items = [(-v, k) for k,v in proc.items()]
        heapq.heapify(items)

        queue = deque()

        while items or queue:
            time += 1

            if items:
                cnt, task = heapq.heappop(items)
                cnt += 1

                if cnt !=0:
                    queue.append( (time + n, (cnt, task)) )

            if queue and queue[0][0] == time:
                _, item = queue.popleft()
                heapq.heappush(items, item)

        return time