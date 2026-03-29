class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(nums) == len(current):
                res.append(current[:])
                return 

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])

                    backtrack(current)

                    current.pop()
                    used[i] = False

        backtrack([])
        return res