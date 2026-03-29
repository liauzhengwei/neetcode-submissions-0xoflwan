class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        sorted_count = dict(sorted(count.items(), key = lambda x:x[1], reverse=True))

        return list(sorted_count.keys())[:k]