class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(start, current, remain):
            if remain == 0:
                res.append(current[:])

            if remain < 0:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                current.append(nums[i])
                bt(i, current, remain - nums[i])
                current.pop()
        bt(0, [], target)
        return res 