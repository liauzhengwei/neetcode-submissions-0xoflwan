class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        sorted_counts = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))

        top_k = list(sorted_counts.keys())[:k]

        return top_k