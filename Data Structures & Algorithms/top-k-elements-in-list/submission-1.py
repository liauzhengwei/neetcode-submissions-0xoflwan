class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]

