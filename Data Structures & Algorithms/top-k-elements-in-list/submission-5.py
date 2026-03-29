class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}

        for num in nums:
            countNums[num] = countNums.get(num, 0) + 1

        # Sorting dictionary: sorted(iterable, key, reverse)
        sortedNums = sorted(countNums.items(), key=lambda x:x[1], reverse = True)

        return [item[0] for item in sortedNums[:k]]


