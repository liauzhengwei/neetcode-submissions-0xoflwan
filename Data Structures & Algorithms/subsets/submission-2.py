class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            # Add current subset to result
            result.append(current[:])

            # Explore all possible next elements
            for i in range(start, len(nums)):
                # Include nums[i]
                current.append(nums[i])

                # Recurse with next starting index
                backtrack(i + 1, current)

                # Backtrack: remove last element
                current.pop()

        backtrack(0, [])
        return result