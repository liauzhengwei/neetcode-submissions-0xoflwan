class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to result
            result.append(path[:])

            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()  # backtrack

        result = []
        backtrack(0, [])
        return result