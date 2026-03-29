class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def bt(current):
            if len(current) == len(nums):
                res.append(current[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    bt(current)
                    current.pop()
                    used[i] = False

        bt([])
        return res