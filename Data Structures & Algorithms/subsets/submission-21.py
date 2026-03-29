class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(start, current):
            res.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                bt(i + 1, current)
                current.pop()
        bt(0, [])
        return res