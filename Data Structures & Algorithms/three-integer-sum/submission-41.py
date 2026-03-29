class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i + 1, n - 1

            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res





def max_transactions(transactions, balance):
    heap = []
    count = 0

    for t in transactions:
        balance += t
        heapq.heappush(heap, t)
        count += 1

        if balance < 0:
            smallest = heapq.heappop(heap)
            balance -= smallest
            count -= 1

    return count

def withdrawal_order(amounts,k):
    q = deque([(i + 1, a) for i,a in enumerate(amounts)])
    result = []

    while q:
        i, amt = q.popleft()
        amt -= k

        if amt > 0:
            q.append((i,amt))
        else:
            result.append(i)

    return result