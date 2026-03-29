class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        maxLength = 0

        for num in set_num:
            if num - 1 not in set_num:
                streak = 1
                current = num
                while current + 1 in set_num:
                    streak += 1
                    current += 1
                maxLength = max(maxLength, streak)

        return maxLength