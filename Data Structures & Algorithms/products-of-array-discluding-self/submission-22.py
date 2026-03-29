class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = 1
        rightprod = 1

        n = len(nums)
        rightarr = n * [1]
        leftarr = n * [1]

        for i in range(n):
            leftarr[i] = leftprod
            leftprod *= nums[i]

        for i in range(n-1,-1,-1):
            rightarr[i] = rightprod
            rightprod *= nums[i]

        res = [leftarr[i] * rightarr[i] for i in range(n)]

        return res