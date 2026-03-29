class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set(nums)

        return len(nodup) != len(nums)