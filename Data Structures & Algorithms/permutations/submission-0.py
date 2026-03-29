class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            # Base case: complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        result = []
        backtrack([])
        return result