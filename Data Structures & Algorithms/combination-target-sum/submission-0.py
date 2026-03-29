class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, current_sum):
            # Base case: found a valid combination
            if current_sum == target:
                result.append(path[:])
                return

            # Base case: exceeded target
            if current_sum > target:
                return

            for i in range(start, len(nums)):
                # Choose num
                path.append(nums[i])                
                # Explore further with same num allowed (i, not i+1)
                
                backtrack(i, path, current_sum + nums[i])
                # Backtrack
                path.pop()

        result = []
        backtrack(0, [], 0)
        return result