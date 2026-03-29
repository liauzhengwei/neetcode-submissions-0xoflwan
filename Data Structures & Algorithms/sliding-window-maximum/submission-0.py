class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maxList = [] * (len(nums) - k + 1)
        windList = [] * k
        currMax = float('-inf')

        for right in range(len(nums)):
            windList.append(nums[right])

            while (right - left + 1) == k:
                currMax = max(windList)
                maxList.append(currMax)

                del windList[0]
                currMax = float('-inf')
                left += 1


        return maxList