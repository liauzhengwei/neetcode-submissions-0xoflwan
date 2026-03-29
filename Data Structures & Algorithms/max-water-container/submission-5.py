class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            smallerH = min(heights[left], heights[right])
            width = right - left

            area = smallerH * width
            maxArea = max(maxArea, area)

            # How to decide which height to move
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea

