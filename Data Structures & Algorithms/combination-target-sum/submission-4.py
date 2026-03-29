class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current, remain):
            if remain == 0:
                res.append(current[:])
                return

            if remain < 0:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, remain - nums[i])
                current.pop()

        backtrack(0, [], target)
        return res