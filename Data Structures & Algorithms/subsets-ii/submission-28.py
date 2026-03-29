class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(start, current):

            res.append(current[:])


            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                current.append(nums[i])
                bt(i + 1, current)
                current.pop()


        bt(0, [])

        return res