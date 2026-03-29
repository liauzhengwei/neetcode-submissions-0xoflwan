class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        maxLength = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                current = num
                streak = 1
                while current + 1 in set_nums:
                    streak += 1
                    current += 1
                maxLength = max(maxLength, streak)

        return maxLength