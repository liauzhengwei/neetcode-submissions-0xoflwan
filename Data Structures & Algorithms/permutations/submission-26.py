class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)

        res = []

        def bt(current):
            if len(current) == len(nums):
                res.append(current[:])

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    bt(current)
                    current.pop()
                    used[i] = False

        bt([])
        return res