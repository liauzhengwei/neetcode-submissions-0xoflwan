class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            smallerH = min(heights[left], heights[right])

            width = right - left

            maxArea =max(maxArea, width * smallerH)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1



        return maxArea