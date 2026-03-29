class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0

        set_num = set(nums)

        for num in nums:
            if num - 1 not in set_num:
                current = num
                streak = 1

                while current + 1 in set_num:
                    current += 1
                    streak += 1
                maxLength = max(maxLength, streak)

        return maxLength