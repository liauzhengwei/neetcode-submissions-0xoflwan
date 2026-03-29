class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            smallerH = min(heights[left], heights[right])
            area = (right - left) * smallerH

            maxArea = max(area, maxArea)

            if heights[right] < heights[left]:
                right -= 1

            else:
                left += 1

        return maxArea