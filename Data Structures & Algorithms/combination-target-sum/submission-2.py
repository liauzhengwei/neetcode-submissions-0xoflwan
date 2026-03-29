class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current, remaining):
            # Found a valid combination
            if remaining == 0:
                res.append(current[:])
                return 

            # No solution
            if remaining < 0:
                return 

            # Try each candidate from 'start' to avoid duplicates
            for i in range(start, len(nums)):
                current.append(nums[i])

                # Use i as can reuse the same element
                backtrack(i, current, remaining - nums[i])

                current.pop()

        backtrack(0, [], target)
        return res